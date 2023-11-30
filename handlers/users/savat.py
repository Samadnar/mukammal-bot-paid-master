from loader import dp, db_book, bot
from aiogram import types
from data.pr import get_books
from keyboards.default.menyu import menyu
from aiogram.dispatcher import FSMContext
from keyboards.inline.for_savat import inline_menyu_btn_1
from aiogram.types import CallbackQuery
from aiogram import Bot, types
from data.pr import FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
@dp.message_handler(text="🛒 Savat")
async def get_info(message: types.Message, state: FSMContext):
    shops = await db_book.get_from_savat(user_id=message.from_user.id)
    if not shops:
        await message.answer("Savatda mahsulot mavjud emas")
    else:
        book_id = []
        number_of_books = []
        price = []
        books = []
        book_name = []
        summa = 0
        for i in shops:
            book_id.append(i[2])
            number_of_books.append(i[3])
        for i in book_id:
            books.append(await db_book.get_one_types_book(id=int(i)))
        for i in books:
            price.append(i[0][3])
            book_name.append(i[0][1])
        for i in range(0, len(price)):
            summa += number_of_books[i] * price[i]
            
        text = ""
        for i in range(0, len(book_name)):
            text += f"<b>{book_name[i]}</b> kitobidan {number_of_books[i]} dona\n"
        text += f"Jami narx <b>{summa}</b> UZS"
        await message.answer(text, reply_markup=inline_menyu_btn_1)
        
        
@dp.callback_query_handler(lambda x: x.data.startswith('Tozalash'))
async  def tozalash(call: CallbackQuery):
    await call.message.answer("Savat tozalandi")
    await db_book.clear_savat_1(call.message.chat.id)
    
@dp.callback_query_handler(text="Tasdiqlash")
async def show_invoices(call: CallbackQuery):
    cl_class = await get_books(call.message.chat.id)
    
    await bot.send_invoice(chat_id=int(call.message.chat.id), **cl_class.generate_invoice(), payload="Kiyimlar")
    # except:
    #     print("Send invoice da xatolik")

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False, error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent" or query.shipping_address.city.lower() == "toshkent" :
        await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING], ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[REGULAR_SHIPPING], ok=True)