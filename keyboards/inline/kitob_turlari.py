from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


# lang_code = CallbackData("vode", "category", "id")

inline_menyu_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Badiiy adabiyotlar", callback_data="1"),
            InlineKeyboardButton(text="Biznes va shaxsiy rivojlanish", callback_data="2")
        ],
        [
            InlineKeyboardButton(text="Bolalar adabiyoti", callback_data="3"),
            InlineKeyboardButton(text="Diniy va ma'rifiy adabiyotlar", callback_data="4") 
        ],
        [
            InlineKeyboardButton(text="Foydali adabiyotlar", callback_data="5"),
            InlineKeyboardButton(text="Ilmiy adabiyotlar", callback_data="6") 
        ]
    ]
)


def example(id, id1, number, data):
    savat_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬅️", callback_data=f"left:{id}-{data}"),
                InlineKeyboardButton(text=f"{id1+1}/{number} ", callback_data="view"),
                InlineKeyboardButton(text="➡️", callback_data=f"right:{id}-{data}")
            ],
            [
                InlineKeyboardButton(text="🛒Savatga qo'shish", callback_data=f"add:{id}-{data}")
            ],
             [
                InlineKeyboardButton(text="⬅️ Ortga", callback_data=f"kitoblar bo'limi")
            ]
        ]
    )
    return savat_btn

def example_1(number, id1, summa, data):
    savat_hisob_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            
            [
                InlineKeyboardButton(text="➖", callback_data=f"minus:{id1}-{data}"),
                InlineKeyboardButton(text=f"{number} dona", callback_data="number of books"),
                InlineKeyboardButton(text="➕", callback_data=f"plus:{id1}-{data}")
            ],
            [
                InlineKeyboardButton(text=f"{summa} UZS", callback_data="summa:{id1}")
            ],
            [
                InlineKeyboardButton(text="❌ Savatni tozalash", callback_data=f"Folse:{id1}-{data}")
            ],
            [
                InlineKeyboardButton(text="⬅️ Ortga", callback_data=f"ortga:{id1}-{data}")
            ]
        ]
    )
    return savat_hisob_btn

