from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnInfo = KeyboardButton('Информация')
btnExit = KeyboardButton('Выход')
btnConfig = KeyboardButton('Старт работы бота')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btnInfo, btnExit)


# otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnExit)
