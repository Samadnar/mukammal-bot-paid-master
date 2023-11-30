from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
inline_menyu_btn_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="Tasdiqlash"),
            InlineKeyboardButton(text="❌ Savatni tozalash", callback_data="Tozalash")
        ]
    ]
)