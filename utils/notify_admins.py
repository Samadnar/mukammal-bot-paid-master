import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi\nKitob qo'shmoq -> /add_books\nFoydalanuvchilarni ko'rmoq -> /view_users")

        except Exception as err:
            logging.exception(err)
