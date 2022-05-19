# import telebot
from lib2to3.pgen2 import token

from pytest import skip
from aiogram import Bot, Dispatcher, executor, types
import config
import youtube_dl
from moviepy.editor import VideoFileClip
import random
import string


# bot = telebot.TeleBot(config.TOKEN)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def lol(message):
    mes = f'<b>Приветсвую тебя, {message.from_user.first_name} {message.from_user.last_name}!</b> Этот бот поможет тебе сделать из видео GIF-ку;)) Просто отправь сюда ссылку на видео и дело в шляпе)0)'
    await bot.send_message(message.from_user.id, mes,  parse_mode='html')


@dp.message_handler()
async def video(message):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(12))

    await bot.send_message(
        message.from_user.id, 'Нужно немного подождать, сначала загружается видео, а потом делается Gif-ка!')
    with youtube_dl.YoutubeDL({'format': 'bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best',  'outtmpl': rand_string, 'merge-output-format': 'mp4'}) as ydl:
        video = ydl.download([message.text])

    await bot.send_message(
        message.from_user.id, 'Осталось совсем немного, уже делаем GIF)')
    clip = (VideoFileClip(rand_string + '.mp4').subclip(1, 5))
    gif = clip.write_gif(rand_string + '.gif')
    await bot.send_animation(message.from_user.id, open(rand_string + '.gif', 'rb'))


# bot.polling(none_stop=True)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
