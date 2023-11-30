from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.product import Product
from loader import  db_book


async def get_books(user_id1):
    
    info_books = await db_book.get_from_savat(user_id=int(user_id1))
    prices_list = []
    
    for pr in info_books:
        prices_purchase_pr = await db_book.get_one_types_book(id=pr["book_id"])
        pr_price = prices_purchase_pr[0][3]
        pr_count = pr[3]
        pr_name = prices_purchase_pr[0][1]

        price_label = LabeledPrice(
                label=f"{pr_name}   {pr_price} so'm * {pr_count} =",
                amount=pr_count*pr_price*100
            )
        prices_list.append(price_label)
        

    
    

    clothes = Product(   
        title="To'lov qilish",
        description="InBazar",
        currency="UZS",
        prices=prices_list,
        start_parameter="create_invoice_clothes",
        photo_url="https://cdn2.iconfinder.com/data/icons/transports-2/200/Untitled-9-1024.png",
        photo_width=1280,
        photo_height=564,
        need_name=True,
        need_phone_number=True,
        need_shipping_address=True,
        is_flexible=True
    )
    return clothes



REGULAR_SHIPPING = types.ShippingOption(
    id='three_day',
    title="3 kunda yetkaziladi",
    prices=[
        LabeledPrice("Maxsus o'ram", 5_000_00),
        LabeledPrice("3 kunda yetkazish xizmati", 10_000_00),
    ]
)


FAST_SHIPPING = types.ShippingOption(
    id='one_day',
    title="1 kunda yetkaziladi",
    prices=[
        LabeledPrice("Maxsus o'ram", 5_000_00),
        LabeledPrice("1 kunda yetkazish xizmati", 30_000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='dokon',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Dastavkasiz", -10_000_00),
    ]
)
# my_book = Product(
#     title="Qamar kitoblar do'koni",
#     description="Kitoblarni sotib olish uchun quyidagi tugmani bosing.",
#     currency= "UZS",
#     prices=[
#         LabeledPrice(
#             label="Kitob",
#             amount=
#         )
#     ]
    
    
    
    
# )