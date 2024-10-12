import asyncio

import Script_dat
import crud_fuctions
from crud_fuctions import get_all_products as get_pr

from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton





api = f'{Script_dat.token_LB}'  # Ключ Telegram-бота
bot = Bot(token=api)  # Обект бота
# Диспатчер для обработки событий
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Расчитать'),
            KeyboardButton('Информация'),
            KeyboardButton('Купить'),
        ]
    ], resize_keyboard=True
)


kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton('Формулы расчёта', callback_data='formulas'),
        ]
    ]
)
kb_inline_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('BCAA', callback_data='product_buying'),
            InlineKeyboardButton('ANABOLS', callback_data='product_buying'),
            InlineKeyboardButton('Set FitMAX', callback_data='product_buying'),
            InlineKeyboardButton('Домашняя еда', callback_data='product_buying')
        ]
    ]
)


crud_fuctions.get_all_products


class UserState(StatesGroup):  # класс параметров
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Это бот для расчета калорий вашего тела.', reply_markup=kb)

@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формулы расчёта калорий:')
    await call.message.answer('Мужчины: 10.0 x Вес + 6.25 x Рост - 5.0 x Возраст + 5')
    await call.message.answer('Женщины: 10.0 x Вес + 6.25 x Рост - 5.0 x Возраст - 161')

@dp.callback_query_handler(text='calories')
async def set_age(call, state):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=int(message.text))
    await message.answer('Укажите свой пол (м\ж):')
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    await UserState.sex.set()
    data = await state.get_data()
    calories_form = 10.0 * data['weight'] + 6.25 * data['growth'] - 5.0 * data['age']
    calories = calories_form + 5 if data['sex'] == 'м' else calories_form - 161
    await message.answer(f'Ваша норма в калориях: {calories}')
    await state.finish()

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Данный бот помогает расчитать вашу норму в калориях.\n'
                        'Для начала введите /start и следуйте инструкциям.')




@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open("imgs/1.jpg", 'rb') as img:
        await message.answer_photo(img, f"Название: {get_pr()[0][1]} | Описание: {get_pr()[0][2]}  | Цена: {get_pr()[0][3]} ")
    with open("imgs/2.jpeg", 'rb') as img:
        await message.answer_photo(img, f"Название: {get_pr()[1][1]}  | Описание: {get_pr()[1][2]}  | Цена: {get_pr()[1][3]} ")
    with open("imgs/3.jpg", 'rb') as img:
        await message.answer_photo(img, f"Название: Set {get_pr()[2][1]}  | Описание: {get_pr()[2][2]}  | Цена: {get_pr()[2][3]} ")
    with open("imgs/4.jpg", 'rb') as img:
        await message.answer_photo(img, f"Название: {get_pr()[3][1]} | Описание: {get_pr()[3][2]} | Цена: {get_pr()[3][3]}")
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline_buy)
    crud_fuctions.connection.close()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)