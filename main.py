import gc
import os
import time

import pytesseract
from PIL import ImageGrab
from PIL import Image
from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

keywords = ["купить","дозор","позиция","buy","sentinel","хочу","лиге"]
bot = Bot(token="TOKEN")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@dp.message_handler()
async def process_start_command(message: types.Message):
    print("Work started")
    await message.answer("Я начал работать, можешь пока отойти за чаем")
    while True:
        time.sleep(8)
        text = str(imToString())
        print(text)
        gc.collect()
        if(text == "" or len(text) < 5):
            continue
        elif any(x in text.lower() for x in keywords):
            await bot.send_photo(message.from_user.id,photo=open("photo.png", 'rb'),caption="Новый трейд? Или скамер?")
        del(text)

def imToString():
    cap = ImageGrab.grab(bbox=(4, 374, 626, 810))
    os.remove("photo.png")
    cap.save("photo.png")
    img = Image.open("photo.png").convert('L')
    tesstr = pytesseract.image_to_string(img,lang='rus')
    del(img,cap)
    return tesstr


if __name__ == '__main__':
    executor.start_polling(dp)