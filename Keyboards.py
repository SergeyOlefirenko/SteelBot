from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
Button_1 = KeyboardButton('Some text')
Button_2 = KeyboardButton('Some text2')
Keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
Keyboard.insert(Button_1)
Keyboard.row(Button_1, Button_2)
Keyboard.add(Button_1, Button_2, Button_1, Button_2, Button_1, Button_2, Button_1, Button_2)
#Русскоязычное меню:

menu = ['Круг', 'Квадрат', 'Труба', 'Лист', 'Балка', 'Швеллер', 'Уголок', 'Шестигранник',
        'Арматура', 'Сфера/шар', 'Слиток',
        'Площадь круга', 'Площадь квадрата/прямоугольника', 'Площадь треугольника',
        'Диагональ фигуры', 'Вписанная фигура', 'Описанная фигура', 'Инлайн клавиатура',
        'Change language']

menu_pipe = ['Круглая', 'Профильная', 'Главное меню']
menu_sheet = ['Марка материала', 'Главное меню']
menu_roundBar = ['Прокат', 'Поковка', 'Блюм/Трубная заготовка', 'Главное меню']
menu_squareBar = ['Прокат', 'Поковка', 'Блюм', 'Главное меню']
menu_beam = ['Номер 10', 'Номер 20', 'Номер 30', 'Номер 36', 'Номер 45', 'Главное меню']
menu_channel = ['Размер 5', 'Размер 6.5', 'Размер 8']
menu_corner = ['№ 4.5', '№ 5', '№ 6', '№ 7']
menu_armature = ['Номер профиля 6', 'Номер профиля 8', 'Номер профиля 10', 'Номер профиля 12']
menu_ingot = ['Кузнечный', 'Прокатный', 'Форменный', 'Блюм', 'Сляб', 'Главное меню']
menu_ingot_forging = ['Многогранный', 'Прямоугольный', 'Круглый', 'Главное меню']
menu_ingot_rolling = ['Круглый', 'Прямоугольный', 'Главное меню']
#Меню для блюма
menu_bloom = ['Круглый', 'Квадратный', 'Прямоугольный', 'Главное меню']
#Меню для сляба
menu_slab = ['Номенклатура', 'Производители', 'Главное меню']
menu_slab_nomenklature = ['Марки материала', 'Геометрические размеры и масса', 'Главное меню']
menu_slab_materials = ['Сталь', 'Сплавы на основе железа', 'Сплавы на основе других металлов',
                       'Цветные сплавы', 'Главное меню']
menu_slab_materials_colour = ['Сплавы на основе титана', 'Сплавы на основе алюминия', 'Сплавы на основе магния', 'Сплавы на основе меди',
                       'Главное меню']
menu_slab_mat_col_ext_titan = ['Марки', 'Геометрические размеры и масса', 'Производители', 'Главное меню']
menu_slab_mat_col_ext_alum = ['Марки', 'Геометрические размеры и масса', 'Производители', 'Главное меню']
menu_slab_mat_col_ext_mag = ['Марки', 'Геометрические размеры и масса', 'Производители', 'Главное меню']
menu_slab_mat_col_ext_cop = ['Марки', 'Геометрические размеры и масса', 'Производители', 'Главное меню']

menu_hexagon = ['Профиль 6', 'Профиль 8', 'Профиль 10', 'Профиль 12']
menu_diagonal = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']
menu_inscribed = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']
menu_described = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']
menu_stainless = ['Главное меню', '12Х18Н10Т', '10Х17Н13М2Т', '08Х18Н10Т', '08Х17Т', '03Х17Н14М2',
                  '03Х18Н11', '04Х18Н10', '12Х18Н9', '08Х18Н10', '12Х17', '12Х13']
menu_stainless_eng = ['Main menu', 'AISI-321H(X12CrNiTi18-9)', 'AISI-316Ti(X6CrNiMoTi17-12-2)',
                      'AISI-321(X6CrNiTi18-10)', 'AISI-439(08Х17Т)', 'AISI-316L(X2CrNiMo18-14-3)',
                      'AISI-316(X5CrNiMo17-12-2)', 'AISI-304L(X2CrNi19-11)', 'AISI-304(X5CrNI18-10)',
                      'AISI-430(X6Cr17)', 'AISI-410(X12CrN13)']
# menu_pipeCounter = ['Марка материала', 'Диаметр Ø', 'Толщина стенки', 'Главное меню']


Keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipe = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_roundBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_squareBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_beam = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_channel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_corner = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_hexagon = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_armature = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_diagonal = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_inscribed = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_described = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_stainless = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipeCounter = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# for i in menu_pipeCounter:
#     Keyboard_menu.insert(i)
for i in menu:
    Keyboard_menu.insert(i)
for i in menu_stainless:
    Keyboard_menu_stainless.insert(i)
for i in menu_pipe:
    Keyboard_menu_pipe.insert(i)
for i in menu_roundBar:
    Keyboard_menu_roundBar.insert(i)
for i in menu_squareBar:
    Keyboard_menu_squareBar.insert(i)
for i in menu_beam:
    Keyboard_menu_beam.insert(i)
for i in menu_channel:
    Keyboard_menu_channel.insert(i)
for i in menu_corner:
    Keyboard_menu_corner.insert(i)
for i in menu_hexagon:
    Keyboard_menu_hexagon.insert(i)
for i in menu_armature:
    Keyboard_menu_armature.insert(i)
for i in menu_diagonal:
    Keyboard_menu_diagonal.insert(i)
for i in menu_inscribed:
    Keyboard_menu_inscribed.insert(i)
for i in menu_described:
    Keyboard_menu_described.insert(i)

#Пример реализации клавиатуры машины состояний:

def kbrd_cat():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Category 1'),
        KeyboardButton('Category 2'))
    return menu


def kbrd_subcat():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Subcategory 1'),
        KeyboardButton('Subcategory 2'))
    return menu


def kbrd_prod():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Product 1'),
        KeyboardButton('Product 2'))
    return menu


def calc_pipe_mm():
    menu_pipe_mm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu_pipe_mm.row(
        KeyboardButton('Марка материала'),
        KeyboardButton('X'),
        KeyboardButton('Operation'),
        KeyboardButton('Y'),
        KeyboardButton('Главное меню'),
    )
    return menu_pipe_mm

# def calc(data: dict):
#     menu = ReplyKeyboardMarkup(resize_keyboard=True)
#     menu.row(
#         KeyboardButton(data['x']),
#         KeyboardButton(data['op']),
#         KeyboardButton(data['y']),
#     )
#     return menu




# def calc_pipe_inch():
#     menu = ReplyKeyboardMarkup(resize_keyboard=True)
#     menu.row(
#         KeyboardButton('Марка материала'),
#         KeyboardButton('Наружный диаметр, inch Ø'),
#         KeyboardButton('Толщина стенки, inch.'),
#     )
#     return menu


menu_materials = ['Нержавеющая сталь', 'Углеродистая сталь', 'Сплавы на основе железа',
                  'Безжелезные сплавы', 'Сплавы на основе алюминия', 'Сплавы на основе магния', 'Сплавы на основе меди']
#Окончание приведенного выше примера:

#Англоязычное меню. Решил реализовать так потому что при работе со словарями - вложенные циклы которые могут вызывать задержку в обработке
# new_menu = []
# for item in menu:
#     word = item.replace(item, 'вася')
#     new_menu.append(word)
# print(new_menu)

menu_english = ['Round Bar', 'Square Bar', 'Pipe', 'Beam', 'Channel', 'Corner', 'Hexagon', 'Armature', 'Sphere/Ball', 'Ingot',
        'Circle square', 'Square/Rectangle square', 'Triangle square',
        'Figure diagonal', 'Inscribed figure', 'Described figure', 'Inline keyboard', 'Change language', 'Main menu']

menu_change_language = ['English', 'Deutsch', 'Italiano', 'Español', 'Français', '日本語', '中國人', '한국인',
                        'Język polski', 'Čeština', 'Slovenský', 'Русский', 'Main menu']

# new_menu = []
# for item in menu:
#     word = item.replace(item, 'вася')
#     new_menu.append(word)
# menu_english1 = new_menu

menu_pipe_en = ['Круглая', 'Профильная', 'Главное меню']
menu_roundBar_en = ['Прокат', 'Поковка', 'Блюм/Трубная заготовка', 'Главное меню']
menu_squareBar_en = ['Прокат', 'Поковка', 'Блюм', 'Главное меню']
menu_beam_en = ['Номер 10', 'Номер 20', 'Номер 30', 'Номер 36', 'Номер 45', 'Главное меню']
menu_channel_en = ['Размер 5', 'Размер 6.5', 'Размер 8']
menu_corner_en = ['№ 4.5', '№ 5', '№ 6', '№ 7']
menu_armature_en = ['Номер профиля 6', 'Номер профиля 8', 'Номер профиля 10', 'Номер профиля 12']
menu_hexagon_en = ['Профиль 6', 'Профиль 8', 'Профиль 10', 'Профиль 12']
menu_diagonal_en = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']
menu_inscribed_en = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']
menu_described_en = ['Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню']



Keyboard_menu_materials = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
for i in menu_materials:
    Keyboard_menu_materials.insert(i)
Keyboard_menu_change_language = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
for i in menu_change_language:
    Keyboard_menu_change_language.insert(i)
Keyboard_menu_english = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu_english:
    Keyboard_menu_english.insert(i)

def inline_keyboard():
    м = 'Марка стали 12Х18Н10Т'
    Button1 = InlineKeyboardButton(text='Марочник сталей', callback_data= str(м))
    Button2 = InlineKeyboardButton(text='Марочник сплавов', callback_data='Button2')
    Button3 = InlineKeyboardButton(text='Круг', callback_data='Button3')
    Button4 = InlineKeyboardButton(text='Picture', callback_data='Picture')
    Button5 = InlineKeyboardButton(text='Кнопка5', callback_data='Button5')
    Button6 = InlineKeyboardButton(text='Кнопка6', callback_data='Button6')
    Button7 = InlineKeyboardButton(text='Кнопка7', callback_data='Button7')
    Keyboard = InlineKeyboardMarkup().add(Button1, Button2, Button3, Button4, Button5, Button6, Button7)
    return Keyboard

#Это меню было тестовым. Оно не работает так как нужно
menu_en = {
    'Круг': 'Round bar',
    'Квадрат': 'Square bar',
    'Труба': 'Pipe',
    'Балка': 'Beam',
    'Швеллер': 'Channel',
    'Уголок': 'Corner',
    'Шестигранник': 'Hexagon',
    'Арматура': 'Armature',
    'Сфера/шар': 'Sphere/Ball',
    'Слиток': 'Ingot',
    'Площадь круга': 'Circle square',
    'Площадь квадрата/прямоугольника': 'Square/Rectangle square',
    'Площадь треугольника': 'Triangle square',
    'Диагональ фигуры':'Figure diagonal',
    'Вписанная фигура':'Inscribed figure',
    'Описанная фигура':'Described figure',
    'Инлайн клавиатура': 'Inline keyboard'
}
pipe = {
    'Круглая':'Round',
    'Профильная':'Profile',
    'Главное меню':'Main menu'
}
roundBar = {
    'Прокат':'Rolling',
    'Поковка':'Forging bar',
    'Блюм/Трубная заготовка':'Bloom/Pipe billet',
    'Главное меню':'Main menu'
}
squareBar = {
    'Прокат':'Rolling',
    'Поковка':'Forging bar',
    'Блюм':'Bloom',
    'Главное меню':'Main menu'
}
beam = {
    'Номер 10':'Number 10',
    'Номер 20':'Number 20',
    'Номер 30':'Number 30',
    'Номер 36':'Number 36',
    'Номер 45':'Number 45',
    'Главное меню':'Main menu'
}
channel = {
    'Размер 5':'5',
    'Размер 6.5':'6.5',
    'Размер 8':'Size 8'
}
corner = {
    '№ 4.5':'№ 4.5',
    '№ 5':'№ 5',
    '№ 6':'№ 6',
    '№ 7':'№ 7'
}
armature = {
'Номер профиля 6', 'Номер профиля 8', 'Номер профиля 10', 'Номер профиля 12'
}
hexagon = {
'Профиль 6', 'Профиль 8', 'Профиль 10', 'Профиль 12'
}
diagonal = {
'Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню'
}
inscribed = {
'Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню'
}
described = {
'Круг', 'Квадрат', 'Прямоугольник', 'Шестигранник', 'Трапеция', 'Главное меню'
}
dict_menu_english = {
    'menu': menu_en,
    'menu_pipe': pipe,
    'menu_roundBar': roundBar,
    'menu_squareBar': squareBar,
    'menu_beam': beam,
    'menu_channel': channel,
    'menu_corner': corner,
    'menu_armature': armature,
    'menu_hexagon': hexagon,
    'menu_diagonal ': diagonal,
    'menu_inscribed': inscribed,
    'menu_described': described
}

# d_items = dict_menu_english.items()
# for item in dict_menu_english.items():
#     # print(item)
#     Keyboard_dict_menu_english.insert(item)
#
# for key in dict_menu_english:
#     # print(key)
#     Keyboard_dict_menu_english.insert(dict_menu_english[key])








