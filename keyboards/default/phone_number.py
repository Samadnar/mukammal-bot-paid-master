from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
phono = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Telefon raqam", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

