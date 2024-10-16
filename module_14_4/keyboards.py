from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Расчитать'),
            KeyboardButton('Информация'),
            KeyboardButton('Купить'),
            KeyboardButton('Регистрация'),
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
