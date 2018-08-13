# Просит ввести пользователя название валют и сумму конвертации. 
# Идет за актуальным курсом на сайт и конвертирует из одной валюты в другую. 

import bs4
import requests

# Создадим словарь валют из файла
currencies = {} # Создали пустой словарь валют
with open("currencies.txt") as file: # Открываем внешний файл со списком валют
    for line in file: # Для каждой строки в файле
        key, value = line.split(';') # Присваиваем значения ключу и значению, разделенными точкой с запятой
        value = value.replace('\n', '') # Так как в каждой строке есть перенос, убираем символ во всех значениях
        currencies[key] = value # Сопоставляем пары Ключ - Значение

def vvod(dict, text1, text2): # Функция, которая будет выполняться пока пользователь не введет желаемое значение из списка или словаря
    user_input = input(text1).upper()
    while user_input not in dict:
        user_input = input(text2)
        user_input = user_input.upper()
    return user_input

v1 = vvod(currencies,
          'Введите название конвертируемоой валюты в формате ISO (например, USD):\n',
          'Мы не нашли такую валюту. Попробуйте еще раз:\n')

v2 = vvod(currencies,
          'Введите название валюты, в которую вы переводите деньги в формате ISO:\n',
          'В мире не существует такой валюты. Попробуйте еще раз:\n')

summ = input('Введите сумму перевода:\n')
while summ.isdigit() == False:
    summ = input('Ввод должен содержать только цифры. Повторите ввод: \n')

url = requests.get('https://freecurrencyrates.com/ru/convert-' + v1 + '-' + v2) # Для конкретного набора валют формируем URL по которому будем брать курс
b = bs4.BeautifulSoup(url.text, "html.parser")

pars = str(b.select('#value_to')) # По CSS селектору получает строку в сыром виде, содержащую наш обменный курс
# Чистим строку от шлака
pars = pars.replace('="', '=')
pars = pars.replace('[<', '')
pars = pars.replace('>]', '')
pars = pars.replace('"/', '')
pars = pars.split('" ')

dict = {} # Создаем промежуточный словарь, из которого в конечном счете достанем значение валюты
for line in pars:
    key, value = line.split('=') # Присваиваем значения ключу и значению, разделенными точкой с запятой
    dict[key] = value # Сопоставляем пары Ключ - Значение

print('Обменный курс из', v1, 'в', v2, 'равняется', dict['value'])
print('Вы обменяли', summ, v1, 'на', float(dict['value'])*float(summ), v2)
