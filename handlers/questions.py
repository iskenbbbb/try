from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


questions_router = Router()


class UserData(StatesGroup):
    name = State()
    email = State()
    phone = State()
    question = State()


@questions_router.message(F.text == "Отмена")
@questions_router.message(Command("cancel"))
async def cancel_questions(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено", reply_markup=ReplyKeyboardRemove())


@questions_router.message(Command("sup"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отмена")]])
    await message.answer(
        "Чтобы задать вопрос введите данные. Если хотите прекратить, нажмите кнопку 'Отмена'"
    )
    await message.answer("Введите ваше имя", reply_markup=kb)


@questions_router.message(F.text, UserData.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserData.email)
    await message.answer("Введите ваш e-mail")


@questions_router.message(F.text, UserData.email)
async def process_email(message: Message, state: FSMContext):
    if not "@" in message.text:
        await message.answer("Введите правильный e-mail")
    elif " " in message.text.strip():
        await message.answer("Введите правильный e-mail")
    else:
        await state.update_data(email=message.text)
        await state.set_state(UserData.phone)
        await message.answer("Напишите свой номер телефона")


@questions_router.message(F.text, UserData.phone)
async def process_email(message: Message, state: FSMContext):
    if isinstance(message.text, int):
        await message.answer("Введите правильный номер телефона")
    elif not "+" in message.text:
        await message.answer("Введите правильный номер, он должен начинатся с +")
    else:
        await state.update_data(email=message.text)
        await state.set_state(UserData.question)
        await message.answer("Задайте вопрос")



@questions_router.message(F.text, UserData.question)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(question=message.text)

    data = await state.get_data()
    # save to DB
    await message.answer(
        "Спасибо. Вот ваши ответы:"
        f"Имя: {data['name']}, email: {data['email']}, ваш вопрос: {data['question']}"
        f"Мы вам ответим как только будем свободны",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


