from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config
class Db_connection_for_book:
    def __init__(self) -> None:
        self.pool : Union[Pool, None] = None
    async def create(self):
            self.pool = await asyncpg.create_pool(
                user = config.DB_USER,
                password = config.DB_PASS,
                host = config.DB_HOST,
                database = config.DB_NAME
            )
    async def execute(self, command, *args,
                          fetch: bool = False,
                          fetchval: bool = False,
                          fetchrow: bool = False,
                          execute: bool = False
                          ):
            async with self.pool.acquire() as connection:
                connection: Connection
                async with connection.transaction():
                    if fetch:
                        result = await connection.fetch(command, *args)
                    elif fetchval:
                        result = await connection.fetchval(command, *args)
                    elif fetchrow:
                        result = await connection.fetchrow(command, *args)
                    elif execute:
                        result = await connection.execute(command, *args)
            return result
    async def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users(
                id  SERIAL PRIMARY KEY,
                telegram_id BIGINT NOT NULL UNIQUE,
                full_name VARCHAR(255) NULL,
                phono_number VARCHAR(255) NULL
            );
        """
        await self.execute(sql, execute=True)

    async def create_table_one(self):
        sql = """
            CREATE TABLE IF NOT EXISTS books(
                id  SERIAL PRIMARY KEY,
                book_name VARCHAR(255) NOT NULL,
                number_of_books BIGINT NOT NULL,
                price_the_books BIGINT NOT NULL,
                image VARCHAR(255) NOT NULL,
                writer_name VARCHAR(255) NOT NULL,
                book_types VARCHAR(255) NOT NULL
            );
        """
        await self.execute(sql, execute=True)
    

        
    async def create_table_two(self):
        sql = """
            CREATE TABLE IF NOT EXISTS savat(
                id  SERIAL PRIMARY KEY,
                user_id BIGINT NULL,
                book_id BIGINT NOT NULL,
                number_of_books BIGINT NOT NULL
            );
        """
        await self.execute(sql, execute=True)
    
    @staticmethod
    def format_srgs(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parametrs.keys(), start=1)
        ])
        return sql, tuple(parametrs.values())
    
    # user jdavali uchun funksiyalar. 
    async def select_all_users(self):
            sql = "SELECT * FROM users;"
            return await self.execute(sql, fetch=True)
    async def add_user(self, telegram_id, full_name, phono_number):
            sql = """
                INSERT INTO users(telegram_id, full_name, phono_number) VALUES($1, $2, $3) returning *
            """
            return await self.execute(sql, telegram_id, full_name, phono_number, execute=True)
    async def get_user_id(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parametrs = self.format_srgs(sql, parametrs=kwargs)
        return await self.execute(sql, *parametrs, fetch=True)
    async def count_users(self):
            sql = "SELECT COUNT(*) FROM users;"
            return await self.execute(sql, fetchval=True)
    
    # books jadvali uchun funksiyalar.    
    async def add_books(self, book_name, number_of_books, price_the_books, image, writer_name, book_types):
            sql = """
                INSERT INTO books(book_name, number_of_books, price_the_books, image, writer_name, book_types) VALUES($1, $2, $3, $4, $5, $6) returning *
            """
            return await self.execute(sql, book_name, number_of_books, price_the_books, image, writer_name, book_types, execute=True)
    async def get_one_types_book(self, **kwargs):
            sql = "SELECT * FROM books WHERE "
            sql, parametrs = self.format_srgs(sql, parametrs=kwargs)
            return await self.execute(sql, *parametrs, fetch=True)
    
   

    
    async def get_from_savat(self, **kwargs):
        sql = "SELECT * FROM savat WHERE "
        sql, parametrs = self.format_srgs(sql, parametrs=kwargs)
        return await self.execute(sql, *parametrs, fetch=True)
    
    async def clear_savat(self, book_id, user_id):
        sql = """
            DELETE FROM savat WHERE user_id = $2 AND book_id = $1;
        """
        return await self.execute(sql, book_id, user_id, execute=True)
   
   
    async def clear_savat_1(self, user_id):
        sql = """
            DELETE FROM savat WHERE user_id = $1;
        """
        return await self.execute(sql, user_id, execute=True)
       

   
        
   
      
    async def update_savat(self, number, book_id, user_id):
        sql = """
            Update savat set number_of_books = $1 where book_id = $2 AND user_id = $3;
        """
        return await self.execute(sql, number, book_id, user_id, execute=True)
    
    async def insert_info(self, user_id, book_id, number_of_books):
        sql = """
            INSERT INTO savat(user_id, book_id, number_of_books) VALUES($1, $2, $3) returning *
        """
        return await self.execute(sql, user_id, book_id, number_of_books, execute=True)