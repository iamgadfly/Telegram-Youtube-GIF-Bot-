import telebot
import config
import youtube_dl
from moviepy.editor import VideoFileClip
import random
import string


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def lol(message):
    mes = f'<b>Приветсвую тебя, {message.from_user.first_name} {message.from_user.last_name}!</b> Этот бот поможет тебе сделать из видео GIF-ку;)) Просто отправь сюда ссылку на видео и дело в шляпе)0)'
    bot.send_message(message.chat.id, mes,  parse_mode='html')


@bot.message_handler()
def video(message):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(12))

    bot.send_message(
        message.chat.id, 'Нужно немного подождать, сначала загружается видео, а потом делается Gif-ка!')
    with youtube_dl.YoutubeDL({'format': 'bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best',  'outtmpl': rand_string, 'merge-output-format': 'mp4'}) as ydl:
        video = ydl.download([message.text])

    bot.send_message(
        message.chat.id, 'Осталось совсем немного, уже делаем GIF)')
    clip = (VideoFileClip(rand_string + '.mp4').subclip(1, 5))
    gif = clip.write_gif(rand_string + '.gif')
    bot.send_animation(message.chat.id, open(rand_string + '.gif', 'rb'))


bot.polling(none_stop=True)
