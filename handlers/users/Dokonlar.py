from aiogram import types
from loader import dp
import requests


@dp.message_handler(text="🏬 Do'konlar")
async def set_shop_location(message: types.Message):
    await message.answer("📍Toshkent shahar, Shayxontohur tumani, Navoiy ko’chasi, 42-uy.\nMo’ljal: Sobiq GUM ro’parasida.\n☎️Bog'lanish uchun:+99899 8454400")
    
@dp.message_handler(text="🏢 Kabinet")
async def set_shop_location(message: types.Message):
    url = 'https://v6.exchangerate-api.com/v6/6001a0d01d53eb9f48cc4884/pair/USD/UZS'
    response = requests.get(url)
    data = response.json()
    kurs = data["conversion_rate"]
    await message.answer(F"1 dollar ($) = {kurs} ming so'm")