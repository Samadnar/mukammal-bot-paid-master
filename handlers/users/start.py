from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.Registratsiya import Registr
from loader import dp, db_book
from aiogram.dispatcher import FSMContext
from keyboards.default.phone_number import phono
from keyboards.default.menyu import menyu



@dp.message_handler(CommandStart(), state=None)
async def check_user(message: types.Message):
    all_users = await db_book.select_all_users()
    n = 0
    for i in all_users:
        if i[1] == message.from_user.id:
            n += 1
    if n == 1:
        await message.answer("Ro'yxatdan o'tgansiz", reply_markup=menyu) 
    else:
        await message.answer(f'''Salom, <b>{message.from_user.full_name}</b>\n Familiya ismingizni kiriting !''')
        await Registr.full_name.set()
    
@dp.message_handler(state=Registr.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(
        {"full_name": message.text}
    )
    await message.answer("Telefon raqam", reply_markup=phono)
    await Registr.tel_number.set()
    
@dp.message_handler(state=Registr.tel_number, content_types=["contact"])
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_number": message.contact.phone_number}
    )
    await message.answer("Ro'yxatdan muvaffaqaiyatli o'tingiz",reply_markup=menyu)
    data = await state.get_data()
    name = data.get("full_name")
    phone = data.get("phone_number")
    await db_book.add_user(message.from_user.id, name, phone)
    await state.finish()
    
    


