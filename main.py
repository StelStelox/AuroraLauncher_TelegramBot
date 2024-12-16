import asyncio
from dynaconf import Dynaconf
from aiogram import Bot, Dispatcher
from aiogram.types import Message

conf = Dynaconf(settings_files='conf/settings.yaml')

dp = Dispatcher()

@dp.message()
async def start_message(message: Message):
    await message.answer('TEST')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    bot = Bot(token=conf.bot.token)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выключен')
        