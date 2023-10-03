from aiogram import types, Router, F
from aiogram.filters import Command
from handlers.texts import START_TEXT
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup


start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                IButton(text="Наш сайт", url="https://google.com"),
                IButton(text="Наш инстаграм", url="https://instagram.com"),
            ],
            [
                IButton(text="О нас", callback_data="about"),
                IButton(text="Подписатся", callback_data="subscribe")
            ],
        ]
    )
    await message.answer(START_TEXT, reply_markup=kb)


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "subscribe")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("О нас")



@start_router.message(Command("photo"))
async def send_photo(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(file)


@start_router.message(Command("info"))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"Привет {message.from_user.first_name}",
    )


