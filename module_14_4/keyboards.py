from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_fuctions import get_all_products as get_pr


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
            InlineKeyboardButton((get_pr()[0][1]), callback_data='product_buying1'),
            InlineKeyboardButton((get_pr()[1][1]), callback_data='product_buying2'),
            InlineKeyboardButton((get_pr()[2][1]), callback_data='product_buying3'),
            InlineKeyboardButton((get_pr()[3][1]), callback_data='product_buying4'),
        ]
    ]
)
