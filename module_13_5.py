from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = '7488208272:AAEvlECQqxi1O8eExlOFjKhHvGLiRNJHuF4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создаем клавиатуру
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_calculate = types.KeyboardButton('Рассчитать')
btn_info = types.KeyboardButton('Информация')
keyboard.add(btn_calculate, btn_info)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)