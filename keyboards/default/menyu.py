from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, callback_query
menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Kitoblar"),
            KeyboardButton(text="🛒 Savat"),
            
        ],
        [
            KeyboardButton(text="🏢 Kabinet"),
            KeyboardButton(text="🏬 Do'konlar"),
        ]
    ],
    resize_keyboard=True
)