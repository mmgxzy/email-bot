import logging
import asyncio
import requests
import schedule
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


logging.basicConfig(
    filename="http_requests.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def perform_request():
    try:
        response = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        response.raise_for_status()

        result = f"Запрос выполнен успешно, статус: {response.status_code}"
        logging.info(result)
        return result
    except requests.RequestException as e:
        logging.error(f"Произошла ошибка: {e}")
        return f"Произошла ошибка: {e}"


@dp.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    await message.answer("Я бот, который выполняет HTTP-запросы каждые 45 секунд.")

@dp.message()
async def not_found(message: Message):
    await message.reply("Я вас не понял")


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


async def scheduled_request():
    result = perform_request()
    await bot.send_message(chat_id=5232082871, text=result)


async def main():
    schedule.every(45).seconds.do(
        lambda: asyncio.ensure_future(scheduled_request())
    )
    asyncio.create_task(scheduler())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
