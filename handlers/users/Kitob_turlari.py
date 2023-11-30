from aiogram import Bot, types
from loader import dp, db_book, bot
from keyboards.default.menyu import menyu 
from aiogram.dispatcher import FSMContext
from keyboards.inline.kitob_turlari import inline_menyu_btn, example, example_1
from aiogram.types import CallbackQuery



@dp.message_handler(text="📚 Kitoblar")
async def get_full_name(message: types.Message, state: FSMContext):
    await message.answer("Sizga kerakli bo'limni tanlang:", reply_markup=inline_menyu_btn)



@dp.callback_query_handler(lambda x: x.data.startswith('right'))
async def qwe(call: CallbackQuery):     

    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    pro_id = call.data.split(":")[-1]
    type_id = call.data[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    n = 0
    a = []
    for i in one_type_book:
        a.append(int(i[0]))
    for i in range(0, len(one_type_book)):
        if int(one_type_book[i][0]) == d_id:
            n = int(i)
    if n+1 == len(one_type_book):
        await call.answer("Kitoblar soni cheklangan")
    else:
        photo = types.input_media.InputMediaPhoto(one_type_book[n+1][4], caption=f"Kitob narxi     {one_type_book[n+1][3]} UZS\nKitobning muallifi      {one_type_book[n+1][5]}")
        await call.message.edit_media(media=photo, reply_markup=example(a[n+1], n+1, len(one_type_book), type_id))
        
@dp.callback_query_handler(lambda x: x.data.startswith('left'))
async def qwe(call: CallbackQuery):  
   
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    pro_id = call.data.split(":")[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    type_id = call.data[-1]
    a = []
    for i in one_type_book:
        a.append(int(i[0]))
    n = 0
    for i in range(0, len(one_type_book)):
       if one_type_book[i][0] == d_id:
           n = int(i)
    if n == 0:
        await call.answer("Kitoblar soni cheklangan")
    else:
        photo = types.input_media.InputMediaPhoto(one_type_book[n-1][4], caption=f"Kitob narxi     {one_type_book[n-1][3]} ZS\nKitobning muallifi      {one_type_book[n-1][5]}")
        await call.message.edit_media(media=photo, reply_markup=example(a[n-1], n-1, len(one_type_book), type_id))

@dp.callback_query_handler(lambda x: x.data.startswith('add'))
async def qwe(call: CallbackQuery):

    pro_id = call.data.split(":")[-1]
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    type_id = call.data[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    number = 1
    book = await db_book.get_from_savat(book_id=d_id, user_id=call.from_user.id)
    book_num = await db_book.get_one_types_book(id=d_id)
    if not book:
        await call.message.edit_reply_markup(reply_markup=example_1(1, d_id, book_num[0][3], type_id))
        await db_book.insert_info(call.from_user.id, d_id, number)
    else:
        summa = book[0][-1] * book_num[0][3]
        await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1], d_id, summa, type_id))

   
@dp.callback_query_handler(text="kitoblar bo'limi")
async def qwe(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Sizga kerakli bo'limni tanlang:", reply_markup=inline_menyu_btn)
    
@dp.callback_query_handler(lambda x: x.data.startswith('plus'))    
async def plus_arg(call: CallbackQuery):

    pro_id = call.data.split(":")[-1]
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    type_id = call.data[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    book = await db_book.get_from_savat(book_id=d_id, user_id=call.from_user.id)
    number = 1
    book_num = await db_book.get_one_types_book(id=d_id)
    summa = book[0][-1] * book_num[0][3]
    book_num = await db_book.get_one_types_book(id=d_id)
    if int(book_num[0][2]) >= int(book[0][-1]) + 1:
        await db_book.update_savat(book[0][-1] + number, d_id, call.from_user.id)
        await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1] + number, d_id, int(summa + book_num[0][3]), type_id))
    else:
        await call.answer("Kitoblar soni chegaralangan")

        
@dp.callback_query_handler(lambda x: x.data.startswith('minus'))
async def minus_arg(call: CallbackQuery):
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    type_id = call.data[-1]
    pro_id = call.data.split(":")[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    book = await db_book.get_from_savat(book_id=d_id, user_id=call.from_user.id)
    number = 1            
    book_num = await db_book.get_one_types_book(id=d_id)
    summa = book[0][-1] * book_num[0][3]
    if 1 <= int(book[0][-1]) - 1:
        await db_book.update_savat(book[0][-1] - number, d_id, call.from_user.id)
        await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1] - number, d_id, int(summa - book_num[0][3]), type_id))
    else:
        await call.answer("Kitoblar soni chegaralangan")    
        
@dp.callback_query_handler(lambda x: x.data.startswith('Folse'))
async def get_sum(call: CallbackQuery):
  
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    pro_id = call.data.split(":")[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    type_id = call.data[-1]
    a = []
    n = 0
    for i in one_type_book:
        a.append(int(i[0]))
    for i in range(0, len(a)):
        if a[i] == d_id:
            n = i
    info = await db_book.clear_savat(d_id, call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=example(d_id, n, len(one_type_book), type_id))

@dp.callback_query_handler(lambda x: x.data.startswith('ortga'))
async def qwe(call: CallbackQuery):
    one_type_book = await db_book.get_one_types_book(book_types=call.data[-1])
    pro_id = call.data.split(":")[-1]
    d_id = pro_id.split("-")[0]
    d_id = int(d_id)
    type_id = call.data[-1]
    a = []
    n = 0
    for i in one_type_book:
        a.append(int(i[0]))
    for i in range(0, len(a)):
        if a[i] == d_id:
            n = i
    await call.message.edit_reply_markup(reply_markup=example(d_id, n, len(one_type_book), type_id)) 
    
     

@dp.callback_query_handler()
async def get_1(call: CallbackQuery):   
    one_type_book = await db_book.get_one_types_book(book_types=f"{call.data}")   
    await call.message.delete()
    await call.message.answer_photo(one_type_book[0][4] , caption=f"Kitob narxi     {one_type_book[0][3]} UZS\nKitobning muallifi      {one_type_book[0][5]}", reply_markup=example(one_type_book[0][0], 0, len(one_type_book), call.data))

    






    




        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# @dp.callback_query_handler(text="2")
# async def get_1(call: CallbackQuery):
#     one_type_book = await db_book.get_one_types_book(book_types="2")
#     await call.message.delete()
#     await call.message.answer_photo(one_type_book[0][4] , caption=f"Kitob narxi     {one_type_book[0][3]} UZS\nKitobning muallifi      {one_type_book[0][5]}", reply_markup=for_2(1, 0, len(one_type_book)))

# @dp.callback_query_handler(lambda x: x.data.startswith('right'))
# async def qwe(call: CallbackQuery):     
#     one_type_book = await db_book.get_one_types_book(book_types="2")
#     pro_id = call.data.split(":")[-1]
#     n = 0
#     a = []
#     for i in one_type_book:
#         a.append(int(i[0]))
#     pro_id = int(pro_id)
#     for i in range(0, len(one_type_book)):
#         if int(one_type_book[i][0]) == int(pro_id):
#             n = int(i)
#     print(a, pro_id, n)
#     if n+1 == len(one_type_book):
#         await call.answer("Kitoblar soni cheklangan")
#     else:
#         photo = types.input_media.InputMediaPhoto(one_type_book[n+1][4], caption=f"Kitob narxi     {one_type_book[n+1][3]} UZS\nKitobning muallifi      {one_type_book[n+1][5]}")
#         await call.message.edit_media(media=photo, reply_markup=for_2(a[n+1], n+1, len(one_type_book)))
    
# @dp.callback_query_handler(lambda x: x.data.startswith('left'))
# async def qwe(call: CallbackQuery):     
#     one_type_book = await db_book.get_one_types_book(book_types="2")
#     pro_id = call.data.split(":")[-1]
#     a = []
#     for i in one_type_book:
#         a.append(int(i[0]))
#     n = 0
#     for i in range(0, len(one_type_book)):
#        if one_type_book[i][0] == int(pro_id):
#            n = int(i)
#     if n == 0:
#         await call.answer("Kitoblar soni cheklangan")
#     else:
#         photo = types.input_media.InputMediaPhoto(one_type_book[n-1][4], caption=f"Kitob narxi     {one_type_book[n-1][3]} ZS\nKitobning muallifi      {one_type_book[n-1][5]}")
#         await call.message.edit_media(media=photo, reply_markup=for_2(a[n-1], n-1, len(one_type_book)))

# @dp.callback_query_handler(lambda x: x.data.startswith('add'))
# async def qwe(call: CallbackQuery):
#     pro_id = call.data.split(":")[-1]
#     number = 1
#     book = await db_book.get_from_savat(book_id=int(pro_id), user_id=call.from_user.id)
#     book_num = await db_book.get_one_types_book(id=int(pro_id))
#     if not book:
#         await call.message.edit_reply_markup(reply_markup=example_1(1, int(pro_id), book_num[0][3]))
#         await db_book.insert_info(call.from_user.id, int(pro_id), number)
#     else:
#         summa = book[0][-1] * book_num[0][3]
#         await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1], int(pro_id), summa))

   
# @dp.callback_query_handler(text="kitoblar bo'limi")
# async def qwe(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Sizga kerakli bo'limni tanlang:", reply_markup=inline_menyu_btn)
    
# @dp.callback_query_handler(lambda x: x.data.startswith('plus'))    
# async def plus_arg(call: CallbackQuery):
#     pro_id = call.data.split(":")[-1]
#     book = await db_book.get_from_savat(book_id=int(pro_id), user_id=call.from_user.id)
#     number = 1
#     book_num = await db_book.get_one_types_book(id=int(pro_id))
#     summa = book[0][-1] * book_num[0][3]
#     book_num = await db_book.get_one_types_book(id=int(pro_id))
#     if int(book_num[0][2]) >= int(book[0][-1]) + 1:
#         await db_book.update_savat(book[0][-1] + number, int(pro_id), call.from_user.id)
#         await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1] + number, int(pro_id), int(summa + book_num[0][3])))
#     else:
#         await call.answer("Kitoblar soni chegaralangan")
        
# @dp.callback_query_handler(lambda x: x.data.startswith('minus'))
# async def minus_arg(call: CallbackQuery):
#     pro_id = call.data.split(":")[-1]
#     book = await db_book.get_from_savat(book_id=int(pro_id), user_id=call.from_user.id)
#     number = 1            
#     book_num = await db_book.get_one_types_book(id=int(pro_id))
#     summa = book[0][-1] * book_num[0][3]
#     if 1 <= int(book[0][-1]) - 1:
#         await db_book.update_savat(book[0][-1] - number, int(pro_id), call.from_user.id)
#         await call.message.edit_reply_markup(reply_markup=example_1(book[0][-1] - number, int(pro_id), int(summa - book_num[0][3])))
#     else:
#         await call.answer("Kitoblar soni chegaralangan")    
        
# @dp.callback_query_handler(lambda x: x.data.startswith('Folse'))
# async def get_sum(call: CallbackQuery):
#     pro_id = call.data.split(":")[-1]
#     one_type_book = await db_book.get_one_types_book(book_types="1")
#     a = []
#     n = 0
#     pro_id = int(pro_id)
#     for i in one_type_book:
#         a.append(int(i[0]))
#     for i in range(0, len(a)):
#         if a[i] == pro_id:
#             n = i
#     info = await db_book.clear_savat(int(pro_id), call.from_user.id)
#     await call.message.edit_reply_markup(reply_markup=example(int(pro_id), n, len(one_type_book)))
 
# @dp.callback_query_handler(lambda x: x.data.startswith('ortga'))
# async def qwe(call: CallbackQuery):
#     pro_id = call.data.split(":")[-1]
#     one_type_book = await db_book.get_one_types_book(book_types="1")
#     a = []
#     n = 0
#     pro_id = int(pro_id)
#     for i in one_type_book:
#         a.append(int(i[0]))
#     for i in range(0, len(a)):
#         if a[i] == pro_id:
#             n = i
#     await call.message.edit_reply_markup(reply_markup=example(int(pro_id), n, len(one_type_book))) 
          
         

        
        
        
        
        
        
        
# @dp.callback_query_handler(text="3")
# async def get_3(call: CallbackQuery):
#     one_type_book = await db_book.get_one_types_book(book_types="Bolalar adabiyoti")
#     for i in one_type_book:
#         await call.message.answer_photo(i[4], caption=f"Kitob narxi >>> {i[3]}\nKitobning muallifi >>> {i[5]}")

# @dp.callback_query_handler(text="4")
# async def get_4(call: CallbackQuery):
#     one_type_book = await db_book.get_one_types_book(book_types="Diniy va ma'rifiy adabiyotlar")
#     for i in one_type_book:
#         await call.message.answer_photo(i[4], caption=f"Kitob narxi >>> {i[3]}\nKitobning muallifi >>> {i[5]}")
        
# @dp.callback_query_handler(text="5")
# async def get_5(call: CallbackQuery):
#     one_type_book = await db_book.get_one_types_book(book_types="Foydali adabiyotlar")
#     for i in one_type_book:
#         await call.message.answer_photo(i[4], caption=f"Kitob narxi >>> {i[3]}\nKitobning muallifi >>> {i[5]}")
        
# @dp.callback_query_handler(text="6")
# async def get_6(call: CallbackQuery):
#     one_type_book = await db_book.get_one_types_book(book_types="Ilmiy adabiyotlar")
#     for i in one_type_book:
#         await call.message.answer_photo(i[4], caption=f"Kitob narxi >>> {i[3]}\nKitobning muallifi >>> {i[5]}")










    
# @dp.message_handler(text="Korzinka")
# async def get_full_name(message: types.Message, state: FSMContext):
#     await message.answer("Salom")
    
# @dp.message_handler(text="Qaytadan registratsiya qilish")
# async def get_full_name(message: types.Message, state: FSMContext):
#     await message.answer("qwerthjgdsdfggd")
  
  

 
    