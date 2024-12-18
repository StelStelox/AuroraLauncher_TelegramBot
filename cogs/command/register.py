import re
from aiogram import F, Router
from aiogram.types import Message
from dynaconf import Dynaconf
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from companent import router, conf
import cogs.keyboards as kb

class Register(StatesGroup):
    login = State()
    password = State()
    numberPhone = State()

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    if message.chat.type != 'private': # Перемещю это в компанент.py
        await message.answer("Эта команда доступна только в личных сообщениях. Пожалуйста, напишите мне в ЛС.")
        return
    await state.set_state(Register.login)
    await message.answer('Введите логин:')

@router.message(Register.login)
async def registing_login(message: Message, state: FSMContext):
    if re.fullmatch(r'[a-z0-9_-]{4,16}', message.text, re.IGNORECASE) is None:
        await message.reply('В вашем нике использует некорректные символы!\nВведите ещё раз:')
        return
    await state.update_data(login=message.text)
    await state.set_state(Register.password)
    await message.answer('Введите пароль:')

@router.message(Register.password)
async def registing_password(message: Message, state: FSMContext):
    if re.fullmatch(r'(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(.{8,})', message.text, re.IGNORECASE) is None: # Нужно переделать фильтр
        await message.reply('Пароль должен быть не мешьше 8 символов, без кириллицы, иметь заглавную букву и спец символ.\nВведите ещё раз')
        return
    await state.update_data(password=message.text)
    await message.delete() # Нет идей как скрывать пароль после ввода
    await state.set_state(Register.numberPhone)  
    await message.answer('Отправьте свой номер телефона', reply_markup=kb.get_number)

@router.message(Register.numberPhone, F.contact)
async def registing_numberPhone(message: Message, state: FSMContext):
    await state.update_data(numberPhone=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Регистрация прошла успешно!\nВот ссылки на лаунчер. Он необходим для игры на сервере', reply_markup=kb.link_launcher)
    await message.answer(f'Ваш логин: {data["login"]}\nПароль: {data["password"]}\nВаш телефон: {data["numberPhone"]}', reply_markup=kb.delete_keyboards()) # Для теста вывожу
    await state.clear()