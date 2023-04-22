# import socket
# print("May be host: 127.0.0.2")
# host = input("Host server: ")
# print("!!!Port must be 0-65535!!!")
# port = int(input("Port server: "))
# HOST = host  # Хост сервера
#
# PORT = port  # Порт сервера
# BUFFER_SIZE = 1024  # Размер буфера сообщений


# import random
# x = 0
# charSymbols = ['q', 'w', 'e', 'r', 't', 'y', 'u'
#         , 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'l'
#         , 'z', 'x', 'c', 'v', 'b', 'n', 'm','0'
#         , '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U'
#         , 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C'
#         , 'V', 'B', 'N', 'M']
# print("Ваш пароль:", end = "")
# while x <=11:
#         y = random.choice(charSymbols)
#         x += 1
#         print(y, end="")
# print("\n")


# import types





from aiogram import Bot, Dispatcher, executor, types
import logging
import requests
from bs4 import BeautifulSoup as BS
from aiogram import types
import os
from aiogram.types import Message, MediaGroup, InputMediaDocument
import random
import re


logging.basicConfig(level=logging.INFO)
TOKEN = "6061328204:AAGfVOGbnf81nGTZX_CDlVTtLI7w5wtQk4E"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

lst_main_dejurnh = ["1. Авагян Карен Грачяевич", "2. Белкин Николай Евгеньевич"
                    ,"2. Белкин Николай Евгеньевич","3. Бобков Михаил Дмитриевич"
                    ,"4. Бойназов Сироджиддин Бахриддинович","5. Волков Алексей Сергеевич"
                    ,"6. Волков Матвей Вадимович","7. Воробьёв Роман Андреевич"
                    ,"8. Гурин Захар Максимович","9. Дрябина Екатерина Александровна"
                    ,"10. Золин Егор Андреевич","11. Иванов Владислав Сергеевич"
                    ,"12. Каримбаев Азиреталы Женишбекович","13. Копаева Варвара Валерьевна"
                    ,"14. Косик Арсений Игоревич","15. Костенко Артём Дмитриевич"
                    ,"16. Машинистов Артём Сергеевич"
                    ," 17. Петров Данила Дмитриевич","18. Прилучный Георгий Константинович"
                    ,"19. Салов Александр Сергеевич","20. Сергеев Алексей Владимирович"
                    ,"21. Сероштанов Никита Сергеевич","22. Скворцов Владислав Витальевич"
                    ,"23. Ташчян Даниил Акопович","24. Цыпляев Егор Андреевич"
                    ]
lst = []

def send_First_Course():
    resp = requests.get("https://collegetsaritsyno.mskobr.ru/uchashimsya/raspisanie-kanikuly")
    bs = BS(resp.text, "html.parser")
    cl = bs.find("div", class_ = "folders")
    cl1 = cl.find_all("li", class_ = "pdf")
    for i in cl1:
        if "Расписание учебных занятий 1 курс с" in i.text:
            pdf_url = "https://collegetsaritsyno.mskobr.ru" + i.a['href']
            lst.append(pdf_url)

            async def send_text(chat_id: int, message_text: str):
                await bot.send_message(chat_id=chat_id, text=message_text)

            @dp.message_handler(commands=['start'])
            async def send_message_handler(message: types.Message):
                chat_id = message.chat.id
                message_text = "Привет, человек! Я James, я буду присылать тебе расписание. " \
                               "Пожалуйста, введите цифру(курс на котором вы находитесь). " \
                               "Для того чтобы я мог точно выдавать расписание!"
                await send_text(chat_id, message_text)


            async def send_text(chat_id: int, message_text: str):
                await bot.send_message(chat_id=chat_id, text=message_text)

            @dp.message_handler(commands=['command1'])
            async def send_message_handler(message: types.Message):
                chat_id = message.chat.id
                message_text = "\n\n".join(lst)
                await send_text(chat_id, message_text)

            @dp.message_handler(commands=['command2'])
            async def send_pdfs(message: Message):
                media = MediaGroup()
                for pdf_url in lst:
                    response = requests.get(pdf_url)
                    filename = pdf_url.split('/')[-1]
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    media.attach(InputMediaDocument(open(filename, 'rb')))
                await message.reply_media_group(media=media)



            @dp.message_handler(content_types=[types.ContentType.ANIMATION])
            async def echo_document(message: types.Message):
                await message.reply_animation(message.animation.file_id)

            @dp.message_handler(commands=['command3'])
            async def echo(message: types.Message):
                await message.answer("https://t.me/+GS-u-4zBq6EzYzgy")


            async def send_text(chat_id: int, message_text: str):
                await bot.send_message(chat_id=chat_id, text=message_text)

            @dp.message_handler(commands=['command4'])
            async def send_message_handler(message: types.Message):
                chat_id = message.chat.id
                message_text1 = random.choices(lst_main_dejurnh, k=2)

                await send_text(chat_id, message_text1)

        else:
            continue



print("BOT start task")

# Если пользовать выбирает опред курс -> в main можно сделать while True для опред. курса. Потому что у кадого пользователя бот имеет свое поведение
def main():
   send_First_Course()

if __name__ == "__main__":
    main()
    executor.start_polling(dp,skip_updates=True)