import i18n
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

API_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', "If you do not want to use Environ, type your token here")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Initialize i18n
i18n.load_path.append('lang')
i18n.set('locale', 'ru')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  """
  Test message to test the bot.
  """
  await message.reply(i18n.t('bot.welcome'))


@dp.message_handler(commands=['keyboard'])
async def send_keyboard(message: types.Message):
  """
  Example of keyboard operation
  """
  button: KeyboardButton = KeyboardButton(i18n.t('bot.keyboard.button'))
  keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    resize_keyboard=True
  )
  
  keyboard.add(button)
  
  await bot.send_message(
    chat_id=message.chat.id,
    text=i18n.t('bot.keyboard.text'),
    reply_markup=keyboard,
  )


@dp.message_handler(text=i18n.t('bot.keyboard.button'))
async def handle_keyboard(message: types.Message):
  """
  Button press processing
  """
  await bot.send_message(
    chat_id=message.chat.id,
    text=i18n.t('bot.keyboard.pressed')
  )

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
