import asyncio
from aiogram import Bot, Dispatcher
from cogs.command.register import router
from companent import router, conf

async def main():
    bot = Bot(token=conf.bot.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nВыключен')