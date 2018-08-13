# Содержит в словаре массив с обменными курсами валют. Просит ввести валюты и сумму для конвертации

kurs = {'usd': {'usd': 1, 'eur': 0.873, 'rub': 66.833, 'kzt': 356.36},
        'eur': {'usd': 1.1454753722795,	'eur': 1,	'rub': 76.54,	'kzt': 408.41},
        'rub': {'usd': 0.0149626681429833,	'eur': 0.0130650640188137,	'rub': 1,	'kzt': 5.332},
        'kzt': {'usd': 0.00280615108317432,	'eur': 0.00244851986973874,	'rub': 0.18754688672168,	'kzt': 1}}

def getCurrencyRate(x, y, z):
    cashout = kurs[y][z] * x
    cashout = '{:.2f}'.format(cashout)
    print('Вы обмениваете', x,  y, 'и получаете', cashout, z, 'по курсу', kurs[y][z])
    return cashout

cashin = input('Введите сумму денег, которую вы хотите поменять\n')
while cashin.isdigit() is not True:
    cashin = input('Необходимо ввести число. Повторите ввод\n')
cashin = int(cashin)

v1 = input('Введите название валюты для обмена. \n(Принимаем только: usd, eur, rub, kzt)\n')
while v1 not in kurs:
    v1 = input('Ошибка при вводе. Введите одно из: usd, eur, rub, kzt\n')
    v1 = v1.lower()

v2 = input('Введите название валюты, которую желаете получить. \n(Принимаем только: usd, eur, rub, kzt)\n')
while v2 not in kurs:
    v2 = input('Ошибка при вводе. Введите одно из: usd, eur, rub, kzt\n')
    v2 = v2.lower()

getCurrencyRate(cashin, v1, v2)
