from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
# from handlers.texts import DRAM_FILMS
from db.queries import get_product_by_category



film_router = Router()


@film_router.message(Command("film"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Фильмы"),
                KeyboardButton(text="Мультфильмы"),
            ],
            [
                KeyboardButton(text="Серилы"),
            ],
        ],
        resize_keyboard=True,
    )
    await message.answer(f"Выберите категирию ниже:", reply_markup=kb)



# обработчик фильмов


@film_router.message(F.text == "Фильмы")
async def show_film(message: types.Message):
    # manga = get_product_by_category(3)
    kb = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="Драма"),
                KeyboardButton(text="Боевик"),
            ],
            [
                KeyboardButton(text="Криминал"),
                KeyboardButton(text="Комедия"),
            ],
            [
                KeyboardButton(text="Фантастика"),
                KeyboardButton(text="Ужасы"),
            ],
        ],
        resize_keyboard = True,
    )
    await message.answer(f"Выберите категирию ниже:", reply_markup=kb)
    # for m in manga:
    #     await message.answer(m[1])




    # пока заглушка

@film_router.message(F.text == "Драма")
async def show_dram(message: types.Message):
    dramm = get_product_by_category(1)
    kb = ReplyKeyboardRemove()
    await message.answer("Список Драм:", reply_markup=kb)
    for d in dramm:
        await message.answer(d[1])

@film_router.message(F.text == "Боевик")
async def show_boev(message: types.Message):
    boev = get_product_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer("Список боевиков:", reply_markup=kb)
    for d in boev:
        await message.answer(d[2])


@film_router.message(F.text == "Криминал")
async def show_criminal(message: types.Message):
    crim = get_product_by_category(3)
    kb = ReplyKeyboardRemove()
    await message.answer("Список криминалов:", reply_markup=kb)
    for d in crim:
        await message.answer(d[3])


@film_router.message(F.text == "Комедия")
async def show_comedy(message: types.Message):
    comm = get_product_by_category(4)
    kb = ReplyKeyboardRemove()
    await message.answer("Список комедий:", reply_markup=kb)
    for d in comm:
        await message.answer(d[4])



@film_router.message(F.text == "Фантастика")
async def show_fantasy(message: types.Message):
    fant = get_product_by_category(5)
    kb = ReplyKeyboardRemove()
    await message.answer("Список фантастика:", reply_markup=kb)
    for d in fant:
        await message.answer(d[5])


@film_router.message(F.text == "Ужасы")
async def show_horror(message: types.Message):
    horror = get_product_by_category(6)
    kb = ReplyKeyboardRemove()
    await message.answer("Список ужасов:", reply_markup=kb)
    for d in horror:
        await message.answer(d[6])



#обработчик мультиков
@film_router.message(F.text == "Мультфильмы")
async def show_multfilm(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="Анимация"),
                KeyboardButton(text="Приключения"),
            ],
            [
                KeyboardButton(text="Мюзикл"),
                KeyboardButton(text="Аниме"),
            ],
            [
                KeyboardButton(text="Фантастика"),
                KeyboardButton(text="Ужасы"),
            ],
        ],
        resize_keyboard = True,
    )
    await message.answer(f"Выберите мультфильм ниже ниже:", reply_markup=kb)



#обработчик мультиков
@film_router.message(F.text == "Анмация")
async def show_animation(message: types.Message):
    anim = get_product_by_category(7)
    kb = ReplyKeyboardRemove()
    await message.answer("Список анимаций:", reply_markup=kb)
    for d in anim:
        await message.answer(d[7])


@film_router.message(F.text == "Приключения")
async def show_advanture(message: types.Message):
    advan = get_product_by_category(8)
    kb = ReplyKeyboardRemove()
    await message.answer("Список приключений:", reply_markup=kb)
    for d in advan:
        await message.answer(d[8])



@film_router.message(F.text == "Мюзикл")
async def show_muskl(message: types.Message):
    muskl = get_product_by_category(9)
    kb = ReplyKeyboardRemove()
    await message.answer("Список мюзиклов:", reply_markup=kb)
    for d in muskl:
        await message.answer(d[9])


@film_router.message(F.text == "Аниме")
async def show_anime(message: types.Message):
    anime = get_product_by_category(10)
    kb = ReplyKeyboardRemove()
    await message.answer("Список аниме:", reply_markup=kb)
    for d in anime:
        await message.answer(d[10])


@film_router.message(F.text == "Фантастика")
async def show_fantasy(message: types.Message):
    funts = get_product_by_category(11)
    kb = ReplyKeyboardRemove()
    await message.answer("Список Драм:", reply_markup=kb)
    for d in funts:
        await message.answer(d[11])


@film_router.message(F.text == "Ужасы")
async def show_mhorror(message: types.Message):
    hor = get_product_by_category(12)
    kb = ReplyKeyboardRemove()
    await message.answer("Список ужасов:", reply_markup=kb)
    for d in hor:
        await message.answer(d[12])