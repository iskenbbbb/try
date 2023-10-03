from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import bot
from aiogram import Router

chat_actions_router = Router()




bad_words = ['анкета', 'ссылка', 'уникальное предложение']


async def echo_ban(message: types.Message):
    ban_words = ["fuck", 'bitch']

    if message.chat.id == -916554410:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"don't say so, u can be banned {message.from_user.username}!")
