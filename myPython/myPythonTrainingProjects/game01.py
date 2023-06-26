string = 'По Борнео и Ямайке ходит слон в трусах и майке'
new_list = list(string)
new_set = set(string)
print('Список из строки: ' + str(new_list))
print('Сет из строки: ' + str(new_set))


monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])



# Обратимся к элементам списка по отрицательным индексам
friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
print(friends[-3])  # Миша
print(friends[-5])  # Сергей

# То же и со строкой
monument_string = 'Я памятник себе воздвиг нерукотворный'
print(monument_string[-2])   # ы
print(monument_string[-37])  # Я




milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)
# Будет напечатано: ['м', 'л', 'к', 'в', 'з']




counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'

# Преобразуем строку в список, а разделителем будет дефис
counter_list = counter_str.split('-')
print(counter_list)

# Создадим ещё одну строку
blok_str = 'Ночь. Улица. Фонарь. Аптека'
# Разобьём фразу по словам.
# Разделителем будет служить сочетание точки и пробела:
blok_list = blok_str.split('. ')
print(blok_list)



poem_str = 'Дама сдавала багаж'

# Применяем к строке метод split(), в скобках указываем пробел в кавычках:
words_list = poem_str.split(' ')
# Печатаем результат:
print(words_list)



message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно')




words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
# Метод join() "склеивает" элементы списка,
# создавая строку, в которой
# элементы исходного списка разделены текстовым символом;
# для разделения применим дефис:
new_string = ' '.join(words_list)

print(new_string)



quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list [-3]

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))



one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

# А без применения f-строк тот же код выглядит похуже:
print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.')


def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')

show_meteo(24, 'облачно')

for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print(f'У вас {messages_count} новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')



def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')  # Аргумент должен содержать f-строку

print_time('19', '28', '06')




def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    summ = 0
    for i in range(len(listened)):
        summ += int(listened[i])
    summ //= 60

    return f'Вы прослушали {len(listened)} песен общей продолжительностью {summ} минут.'


print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))





# Импорт библиотеки math.
import math

# Теперь в программе можно применять любые функции из неё.
square_root = math.sqrt(16)
print(square_root)




from random import choice  # Импорт одной функции из библиотеки

def find_a_present(prizes):
    # Обращаемся к функции напрямую: choice(), а не random.choice()
    return choice(prizes)

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))




import random as r

# Теперь к библиотеке random нужно обращаться только через псевдоним r:
print(r.randint(0, 100)) # Случайное целое число от 0 до 100



# Подключите библиотеку random и дайте ей краткое имя
from random import choice as ch

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    # Напишите ваш код здесь
    return ch(answers)


print(how_are_you())




import datetime as dt

# Взлёт: 1961 год, 12 апреля, 9 часов утра, 7 минут
start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

print('Уже', start_time, 'Поехали!')



import datetime as dt

start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

# Дата и время посадки: 1961 год, 12 апреля, 10 часов, 55 минут
landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)

print(landing_time - start_time)




import datetime as dt

# Дата выхода первой серии.
start_time = dt.datetime(2011, 4, 17)
# Укажите дату выхода последней серии.
final_time = dt.datetime(2019, 4, 15)

# Вычислите, сколько времени шёл сериал.
duration = final_time - start_time

print(duration)



import datetime as dt

utc_time = dt.datetime.utcnow()
print(utc_time)



import datetime as dt

# Как и раньше - определяем текущее время UTC
utc_time = dt.datetime.utcnow()

# Создаём промежуток времени в три часа
period = dt.timedelta(hours=3)

# И прибавляем к значению времени по UTC поправку в три часа:
moscow_time = utc_time + period

# Печатаем
print(moscow_time)




import datetime as dt

# Время, за которое Боттас сделал круг — это не дата,
# а продолжительность, промежуток времени. Создаём данные типа timedelta:
time_bottas = dt.timedelta(minutes=1, seconds=25, microseconds=273250)

# Вычисляем timedelta Хэмилтона:
time_hamilton = time_bottas + dt.timedelta(microseconds = 208860)

print(time_hamilton)

import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(city):
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city
    time = dt.datetime.utcnow() + dt.timedelta(hours=UTC_OFFSET[city])
    return time


print(what_time('Екатеринбург'))



import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    sity = DATABASE[friend]
    time = dt.datetime.utcnow() + dt.timedelta(hours=UTC_OFFSET[sity])
    return time

print(what_time('Соня'))




import datetime as dt

# дата первого осеннего снега в Новосибирске в 2018
first_snow = dt.datetime(2018, 9, 9)

# дата последнего весеннего снега в Новосибирске в 2018
last_snow = dt.datetime(2018, 5, 19)

print(last_snow.strftime('Последний снег выпал в %U-ю неделю года.'))
print(first_snow.strftime('А первый снег пошёл в %U-ю неделю.'))





user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' + '%20'.join(user_query.split())

print(url)



import urllib.parse

url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
# чтобы вычленить текст вопроса
# разбейте строку по знаку = и возьмите
# второй элемент получившегося списка
question = (url.split('=')[1]) # сохраните его в переменной question
# напечатайте на экран запрос в расшифрованном виде
print(urllib.parse.unquote(question))  # ваш код здесь