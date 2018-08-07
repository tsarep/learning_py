# Напишите программу хам-фильтр, в которой будут заменяться ругательные слова из списка 
# на на приличную альтернативу, 
# как в фильме "джентельмены удачи" редиска -> не хороший человек.

mat = {} # Создали пустой словарь матов
with open("mat.txt") as file: # Открываем внешний вайс со списком матов
    for line in file: # Для каждой строки в файле
        key, value = line.split(';') # Присваиваем значения ключу и значению, разделенными точкой с запятой
        value = value.replace('\n', '') # Так как в каждой строке есть перенос, убираем символ во всех значениях
        mat[key] = value # Сопоставляем пары Ключ - Значение

badtext = input('Введите плохой текст:\n') # Просим пользователя ввести плохой текст

def cenzor(inp): # Функция Цензор
    inp2 = inp.split(' ') # Преобразуем строку в список
    x = 0
    while x < len(inp2): # Пока Х меньше количества слов в строке
        badword = inp2[x].lower() # Приводим строки к нижнему регистру
        if badword in mat: # Проверяем, есть ли плохое слово в нашем словаре
            inp2[x] = mat[badword] # Если есть - заменяем его на значение из словаря
        else:
            x += 1 # Иначе увеличиваем индекс и идем проверять следующее слово
    inp2 = ' '.join(inp2) # Объединяем все строки из списка (некоторые замененные) обратно в одну
    return inp2 # Функция возвращает значение строки с учетом цензуры

goodtext = cenzor(badtext) # Получаем хороший текст

print(goodtext) # Выводим его на экран