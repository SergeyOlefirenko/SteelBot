from aiogram import Bot, Dispatcher, executor, types
import os
import sqlite3
import Keyboards as kb
import requests
TOKEN = os.environ['token']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
users = {}
print(TOKEN)
#Создаем таблицы для базы данных
def create_users():
    connect = sqlite3.connect('chatUsers_database.db')
    cursor = connect.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Users('
        'UserID integer primary key,'
        'Firstname text,'
        'Lastname text,'
        'Birthday text,'
        'Phone text,'
        'Mail text'
        ');'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Messages('
        'UserID integer,'
        'MessageID integer primary key autoincrement,'
        'TextMessage text'
        ');'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS SteelGrades('
        'UserID integer,'
        'QuantityOfApply integer primary key autoincrement,'
        'UserRequestText text,'
        'SteelGrades,'
        'ChemicalComposition,'
        'MechanicalProperties,'
        'ThermalTreatment'
        ');'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Prices('
        'UserID integer,'
        'QuantityOfApply integer primary key autoincrement,'
        'UserRequestText text,'
        'LME,'
        'Traders,'
        'Producers,'
        'FOB'
        ');'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Taxes('
        'UserID integer,'
        'QuantityOfApply integer primary key autoincrement,'
        'UserRequestText text,'
        'Countries'
        ');'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Countries('
        'Country text,'
        'Language text,'
        'Material text,'
        'SteelGrades text,'
        'Traders,'
        'Producers,'
        'FOB'
        ');'
    )
    connect.commit()
    cursor.close()


create_users()


def get_user_by_id(user_id):
    connect = sqlite3.connect('chatUsers_database.db')
    cursor = connect.cursor()
    request_in_db = f'SELECT * from Users where UserID = {user_id} '
    user = cursor.execute(request_in_db).fetchall()
    connect.commit()
    cursor.close()
    return user


def update_user_by_id(user_id, text_message):
    connect = sqlite3.connect('chatUsers_database.db')
    cursor = connect.cursor()
    request_in_db = f"UPDATE Users SET 'TextMessage' = {text_message} where UserID = {user_id}"
    cursor.execute(request_in_db)
    connect.commit()
    cursor.close()

def insert_user(user: dict):
    connect = sqlite3.connect('chatUsers_database.db')
    cursor = connect.cursor()
    request_in_db = f'INSERT INTO Users (UserID, Firstname, Lastname, Birthday,Phone, Mail) VALUES ("{user["UserID"]}",' \
                    f' "{str(user["Firstname"])}", "{str(user["Lastname"])}", "{str(user["Birthday"])}",' \
                    f'"{str(user["Phone"])}", "{str(user["Mail"])}");'
    cursor.execute(request_in_db)
    connect.commit()
    cursor.close()

def insert_message(message: dict):
    connect = sqlite3.connect('chatUsers_database.db')
    cursor = connect.cursor()
    request_in_db = f'INSERT INTO Messages (UserID, TextMessage) VALUES ("{message["UserID"]}",' \
                    f'"{str(message["TextMessage"])}");'
    cursor.execute(request_in_db)
    connect.commit()
    cursor.close()

# Первый хендлер для обработки клавиатуры:

@dp.message_handler()
async def recording(message: types.Message):
    print(message)
    user = get_user_by_id(message.from_user.id)
    if len(user) == 0:
        insert_user({"UserID": message.from_user.id, "Firstname": message.from_user.first_name,
                     "Lastname": message.from_user.last_name, "Birthday": None,
                     "Phone": None, "Mail": None})
    insert_message({"UserID": message.from_user.id, "TextMessage": message.text})
    print('\n', 'User ID:', message.from_user.id, '\n',
          'User name:', message.from_user.first_name,
          message.from_user.last_name, '\n',
          'Wrote:', message.text, '\n',
          'ChatID:', message.message_id, '\n',
          'Language:', message.from_user.language_code)
    users.update({message.from_user.id: message.from_user.first_name})
    if message.text == 'X' or 'Operation' or 'Y' and message.text != 'Главное меню':
        await calculator(message)
        await message.delete()
    if message.text == 'Прокат':
        await message.answer(text=f'Введите параметры:')
    if message.text == 'Поковка':
        await message.answer(text=f'Введите размеры:')
    if message.text == 'Блюм/Трубная заготовка':
        await message.answer(text=f'Введите размеры:')
    if message.text == 'Блюм':
        await message.answer(text=f'Введите размеры:')
    if message.text == 'Профильная':
        await message.answer(text=f'Введите размеры:')
    if message.text == 'Номер 10':
        await message.answer(text=f'9.47 кг/м.')
    if message.text == 'Номер 20':
        await message.answer(text=f'21.26 кг/м.')
    if message.text == 'Номер 30':
        await message.answer(text=f'50.2 кг/м.')
    if message.text == 'Инлайн клавиатура':
        keyboard = kb.inline_keyboard()
    else:
        keyboard = kb.Keyboard_menu
    if message.text == 'Круглая':
        keyboard = kb.calc_pipe_mm()
    if message.text == 'Марка материала':
        keyboard = kb.Keyboard_menu_materials
    if message.text == 'Нержавеющая сталь':
        keyboard = kb.Keyboard_menu_stainless
# Добавление фото (просто тестовый код для проверки при вводе приветствия):
    if message.text == 'Hi':
        await bot.send_photo(chat_id=message.from_user.id, photo=types.InputFile('sobach.jpg'))
# Код для выбора языка пользователем:
    if message.text == 'Change language':
        keyboard = kb.Keyboard_menu_change_language
# Этот код работает для автоматической смены языка меню но не подключаются словари. Нужно разбираться.
# В общем со словарями разобрался - здесь нужно использовать списки.
# Ввиду необходимости заполнения списка из словарей решил этот способ не использовать за ненадобностью, а обращаться сразу к спискам.
    # if message.text == 'Change language' and message.from_user.language_code == 'en':
    #     keyboard = kb.Keyboard_menu_english
# Этот код подключает англоязычное меню. Все субменю также подтягиваются автоматически уже на английском.
# То же самое будет реализовано и на других языках. Пока все в тестовом режиме. Меню выбора языка уже реализовано на нескольких языках.
    if message.text == 'Главное меню':
        await message.answer(message.text, reply_markup=keyboard)
        # if message.text == 'Change language' and message.from_user.language_code == 'en':
        #     keyboard = kb.Keyboard_menu_english
    if message.text == 'English':
        keyboard = kb.Keyboard_menu_english
    if message.text == 'Круг':
        keyboard = kb.Keyboard_menu_roundBar
    if message.text == 'Квадрат':
        keyboard = kb.Keyboard_menu_squareBar
    if message.text == 'Труба':
        keyboard = kb.Keyboard_menu_pipe
    if message.text == 'Балка':
        keyboard = kb.Keyboard_menu_beam
    if message.text == 'Швеллер':
        keyboard = kb.Keyboard_menu_channel
    if message.text == 'Уголок':
        keyboard = kb.Keyboard_menu_corner
    if message.text == 'Шестигранник':
        keyboard = kb.Keyboard_menu_hexagon
    if message.text == 'Арматура':
        keyboard = kb.Keyboard_menu_armature
    if message.text == 'Диагональ фигуры':
        keyboard = kb.Keyboard_menu_diagonal
    if message.text == 'Вписанная фигура':
        keyboard = kb.Keyboard_menu_inscribed
    if message.text == 'Описанная фигура':
        keyboard = kb.Keyboard_menu_described
    await message.answer(message.text, reply_markup=keyboard)
#Этот код не работает вообще. Нужно разбираться как удалять сообщения бота...
    # await bot.delete_message(message.answer(message.text), message.message_id)
#Писал просто для теста(выводит счетчик количества запросов/ответов самого чата)
    # await message.answer(message.message_id, reply_markup=keyboard)
    text = f'User {message.from_user.first_name} wrote {message.text}'
    for i in users.keys():
        if i != message.from_user.id:
            await bot.send_message(chat_id=i,
                                   text=text)
#Пробую запустить обработчик уже в двадцать пятый, наверное, раз...(((
# if message.text == 'X' or 'Operation' or 'Y':
    #     await calculator(message)

        # if message.text == 'X' or 'Operation' or 'Y' and message.text != 'Главное меню':
        #     await calculator(message)
        # else:
        #     await recording(message)
# Получилось вызвать хендлер как функцию только с другой асинхронной функции, а не отдельно.
# Почему так, если логика чтения кода не нарушалась - остается загадкой. Пробую разобраться
# так как для меня это важно.

# Машина состояний:
# Есть проблемы с пониманием работы так как результат выводится всегда по разному.
# Не могу понять как устранить проблему с переключением на другое меню при вводе данных,
# при обращении к функции "calculator". Три дня потрачено на поиски решения - пока результат
# не очень, хотя и разобрался с вызовом этой функции так, чтобы и другие функции отрабатывали
# при обращении к ним. До этого, при вызове данной функции, остальные попросту не работали...

class State:
    states = [
        'основное меню',
        'ввод х',
        'ввод оператора',
        'ввод y',
    ]
    data = {
        'x': 'X',
        'y': 'Y',
        'op': 'operator',
    }
    state = ''

    def __init__(self):
        self.state = self.states[0]

    def __str__(self):
        return f'\n***\n{self.data}\n{self.state}\n***\n'


# В этом словаре в качестве ключа будет user_id из telegram, а в качестве значения - State
users_new = {}

@dp.message_handler()
async def calculator(message: types.Message):
    chat_id = message.from_user.id
    if users_new.get(chat_id) is None:
        users_new.update({chat_id: State()})
    if message.text == 'X':
        users_new[chat_id].state = State().states[1]
        text = 'Input X'
    elif message.text == 'Operation':
        users_new[chat_id].state = State().states[2]
        text = 'Input operator'
    elif message.text == 'Y':
        users_new[chat_id].state = State().states[3]
        text = 'Input Y'
    else:
        if users_new[chat_id].state == State().states[1]:
            users_new[chat_id].data['x'] = message.text
        elif users_new[chat_id].state == State().states[2]:
            users_new[chat_id].data['op'] = message.text
        elif users_new[chat_id].state == State().states[3]:
            users_new[chat_id].data['y'] = message.text
        users_new[chat_id].state = State().states[0]
        text = f'{users_new[chat_id].data["x"]} {users_new[chat_id].data["op"]} {users_new[chat_id].data["y"]}'
    await bot.send_message(chat_id, text, reply_markup=kb.calc_pipe_mm())
    print(f'{chat_id}-{message.from_user.username}', users_new[chat_id])
# Реализация хендлера инлайн-клавиатуры. Все работает в тестовом режиме.
@dp.callback_query_handler()
async def call_echo(callback_q: types.CallbackQuery):
    print(callback_q)
    await bot.answer_callback_query(callback_q.id, text='Марочник стали и сплавов')
    await bot.send_message(chat_id=callback_q.from_user.id, text=callback_q.data)


if __name__ == '__main__':
    executor.start_polling(dp)
