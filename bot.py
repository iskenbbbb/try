from decouple import config
from os import getenv
from aiogram import Bot, Dispatcher



TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)