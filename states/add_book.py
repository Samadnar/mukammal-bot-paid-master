from aiogram.dispatcher.filters.state import StatesGroup, State
class Add_book(StatesGroup):
    book_name = State()
    number_of_books = State()
    price_the_book = State()
    image = State()
    writer_name = State()
    types = State()
    
    