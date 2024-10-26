# -- coding: utf8 --


import logging
import asyncpg
from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
import asyncio


BOT_TOKEN = '7564082109:AAFrn4G_3h0rHqjogJo4UyXuXJB6Gda-zDU'
DATABASE_CONFIG = {
    'user': 'postgres',
    'password': '24651asd',
    'database': 'Ogetto',
    'host': 'localhost'
}

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def update_tg_id(referral_code: int, user_id: int):
    try:
        conn = await asyncpg.connect(**DATABASE_CONFIG)
        query = "UPDATE authentication_user SET tg_id = $1 WHERE id = $2"
        print(referral_code, user_id)
        await conn.execute(query, int(user_id), int(referral_code),)
        await conn.close()
    except Exception as e:
        logging.error(f"Error updating tg_id: {e}")


@dp.message(CommandStart())
async def start_command(message: types.Message):
    args = message.text.split(' ')
    # args = message.get_args()
    user_id = message.from_user.id

    if len(args) == 2:
        await message.answer(f"Привет, теперь ты сможешь получать увеломления о предстоящих событиях, итогам челенджей и т.д")
        await update_tg_id(referral_code=args[-1], user_id=user_id)
    else:
        await message.answer("Привет! Ты пришёл без диплинка, перейди по ссылке из личного кабинета")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    # bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())