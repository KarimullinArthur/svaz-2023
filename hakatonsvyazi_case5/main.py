import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import *
from MyApi import MyApi

client: MyApi = MyApi(TOKEN_DADATA)
logging.basicConfig(level=logging.INFO)
bot: Bot = Bot(token=TOKEN_TELEGRAM)
dp: Dispatcher = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def cmd_start(message: types.Message):
    try:
        coordinates: list = message.text.split(",")
        dates: list = client.getPostByCoordinates(coordinates[0], coordinates[1])
        if len(dates) != 0:
            await message.answer("На{} работает почтовое отделение Почты России c индексом {} и адресом: {} ".format(dates[0], dates[1], dates[2]))
        else:
            await message.answer("Извините, по вашему адресу не нашлось отделений Почты России. Попробуйте другие координаты")
    except Exception as e:
        await message.answer("Проверьте правильность введенных координат")
        print(e)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())