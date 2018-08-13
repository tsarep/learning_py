# Производит анализ курса валют за последние X дней. 
# Выводит историю курса по выбранной валюте, показывает средний курс и коэффициент вариации

import bs4
import requests
import math

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

#v1 = 'USD'
v1 = vvod(currencies,
          'Введите название конвертируемоой валюты в формате ISO (например, USD):\n',
          'Мы не нашли такую валюту. Попробуйте еще раз:\n')
#v2 = 'KZT'
v2 = vvod(currencies,
          'Введите название валюты, в которую вы переводите деньги в формате ISO:\n',
          'В мире не существует такой валюты. Попробуйте еще раз:\n')

days = input('За сколько дней вам показать курс валюты?\n')
while days.isdigit() == False:
    days = input('Ввод должен содержать только цифры. Повторите ввод: \n')
days = int(days)

url = requests.get('https://freecurrencyrates.com/ru/exchange-rate-history/' + v1 + '-' + v2 + '/2018/fcr') # Для конкретного набора валют формируем URL по которому будем брать курс
b = bs4.BeautifulSoup(url.text, "html.parser")
pars = str(b.select('.one-month-data-cell .one-month-data-rate'))
pars = pars.replace('<div class="one-month-data-rate">', '')
pars = pars.replace('[', '')
pars = pars.replace(']', '')
pars = pars.split('</div>, ')


def sr_ar(kol_vo, list): # Функция вычисляет среднее арифмитическое для первых X значений из списка
    i, s = 0, 0
    while i < kol_vo:
        s = s + float(list[i])
        i += 1
    s = s / kol_vo
    return s

def sr_kv(kol_vo, sr_ar, list): # Функция вычисляет среднеквадратичное отлонение для первых Х значений из списка
    i, s = 0, 0
    while i < kol_vo:
        s = s + math.pow((float(list[i]) - sr_ar), 2)
        i += 1
    s = s / kol_vo
    s = math.sqrt(s)
    return s

def kof_var(sr_kv,sr_ar): # Функция вычисляет коэффициент вариации
    s = sr_kv / sr_ar * 100
    return s

sr_ariph = sr_ar(days,pars)
sr_kv_otkl = sr_kv(days, sr_ariph, pars)
ko_va = kof_var(sr_kv_otkl, sr_ariph)

print('На сегодня обменный курс из {} в {} равняется {}'.format(v1,v2,pars[0]))
print('История курса валюты за последние {} суток: {}'.format(days,pars[0:days]))
print('Cредний курс {} за этот период составил {:.2f} {}'.format(v1,sr_ariph, v2))
print('Коэффициент вариации равен {:.2%}'.format(ko_va))
pars[days] = float(pars[days])
pars[0] = float(pars[0])
if pars[days] < pars[0]:
    print('Курс {} увеличился за последние {} суток на {:.2f} {}, то есть на {:.2%}'.format(v1,days,pars[0]-pars[days],v2,pars[0]/pars[days]-1))
else:
    print('Курс {} уменьшился за последние {} суток на {:.2f} {}, то есть на {:.2%}'.format(v1,days,pars[days]-pars[0],v2,pars[days]/pars[0]-1))
print('P.S. На основании данных free currency rates https://freecurrencyrates.com/ru/exchange-rate-history/{}-{}/2018'.format(v1,v2))
