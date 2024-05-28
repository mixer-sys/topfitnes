import asyncio

from aiogram import Bot, Dispatcher

from core import start_logging
from local_settings import API_TELEBOT_KEY
from calories_and_bju import commands
from user import handlers
from sleep import handlers as sleep_handlers
from workoutsession import handler as workoutsession_handlers
from calories_bju import handlers as calories_handlers

logger = start_logging()
logger.info('Start logging')

bot = Bot(token=API_TELEBOT_KEY)

dp = Dispatcher()


"""@dp.callback_query(F.data == 'callories_cpf')
async def callories_cpf(callback: types.CallbackQuery):
    await callback.message.answer(
        'Каллории и БЖУ'
    )"""


async def main():
    dp.include_router(handlers.user_router)
    dp.include_router(sleep_handlers.sleep_router)
    dp.include_router(workoutsession_handlers.form_router)
    dp.include_router(calories_handlers.bju_router)
    # dp.include_router(commands.router)

    dp.include_router(commands.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
