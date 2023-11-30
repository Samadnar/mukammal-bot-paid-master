from aiogram.dispatcher.filters.state import StatesGroup, State
class Registr(StatesGroup):
    full_name = State()
    tel_number = State()
