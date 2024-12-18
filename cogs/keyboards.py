from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from companent import conf
get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить номер телефона', request_contact=True)]
    ],
    resize_keyboard=True
)
link_launcher = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Windows 10/11', url=f'{conf.web.url_launcher_windows}')],
        [InlineKeyboardButton(text='MacOS', url=f'{conf.web.url_launcher_macos}')],
        [InlineKeyboardButton(text='Linux', url=f'{conf.web.url_launcher_linux}')]
    ]
)
delete_keyboards = ReplyKeyboardRemove

# Возможно перемешю это всё в компаненты.py