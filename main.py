
import asyncio
import logging
from bot import bot, dp
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.film import film_router
from handlers.questions import questions_router
# from db.sql_commans import Database
from db.queries import init_db, create_tables, populate_tables


async def on_startup():
    # Database().sql_create_db()
    init_db()
    create_tables()
    populate_tables()

async def main():
    dp.startup.register(on_startup)
    dp.include_router(start_router)
    dp.include_router(film_router)
    dp.include_router(questions_router)

    dp.include_router(echo_router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
