from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = '7488208272:AAEvlECQqxi1O8eExlOFjKhHvGLiRNJHuF4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создаем обычную клавиатуру с кнопками
main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_calculate = types.KeyboardButton('Рассчитать')
btn_info = types.KeyboardButton('Информация')
btn_buy = types.KeyboardButton('Купить')
main_kb.add(btn_calculate, btn_info, btn_buy)

# Создаем Inline клавиатуру для продуктов
products_kb = types.InlineKeyboardMarkup(row_width=2)
products_buttons = [
    types.InlineKeyboardButton(f"Product{i}", callback_data="product_buying")
    for i in range(1, 5)
]
products_kb.add(*products_buttons)

# Создаем Inline клавиатуру
inline_kb = types.InlineKeyboardMarkup(row_width=1)
btn_calc_calories = types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn_show_formulas = types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(btn_calc_calories, btn_show_formulas)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', 
                        reply_markup=main_kb)


@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data == 'formulas')
async def get_formulas(call):
    formula_text = """Формула Миффлина-Сан Жеора для расчета суточной нормы калорий:

Для мужчин:
(10 × вес в кг) + (6.25 × рост в см) - (5 × возраст) + 5"""
    await call.message.answer(formula_text)
    await call.answer()


@dp.callback_query_handler(lambda c: c.data == 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Формула Миффлина-Сан Жеора для мужчин
    calories = (10 * float(data['weight']) +
                6.25 * float(data['growth']) -
                5 * float(data['age']) + 5)

    await message.answer(f'Ваша суточная норма калорий: {calories:.0f} ккал')
    await state.finish()


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(
            f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        )
        with open(f'{i}.jpg', 'rb') as photo:
            await message.answer_photo(photo)
    
    await message.answer("Выберите продукт для покупки:", 
                        reply_markup=products_kb)


@dp.callback_query_handler(lambda c: c.data == "product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(lambda message: message.text == 'Информация')
async def show_info(message):
    await message.answer('Это бот для расчета нормы калорий и покупки продуктов. '
                        'Используйте кнопку "Рассчитать" для подсчета нормы калорий '
                        'или кнопку "Купить" для просмотра доступных продуктов.')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
