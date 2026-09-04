from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
import asyncio
from handlers.commands import router as cmd_router
from aiogram.types import BotCommand


bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(cmd_router)


bot_cmds = [
    BotCommand(command='start',description='wake up the bot and registration'),
    BotCommand(command='add',description='add task'),
    BotCommand(command='task_list',description='show task list'),
    BotCommand(command='help', description='help')
]

async def main():
    await bot.set_my_commands(bot_cmds)
    await dp.start_polling(bot)


asyncio.run(main())