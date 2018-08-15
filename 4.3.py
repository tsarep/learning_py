def printSimpleNumbers(numbers):
    '''
    Функция выведет и вернет список простых чисел от единицы до указанного пользователем числа согласно алгоритму поиска "Решето Эратосфена"
    :param numbers: до какого числа будет производиться поиск простых чисел
    :return: Список простох чисел от 1 до numbers
    '''
    rangeInt = list(range(2, numbers))
    index = 0
    while index < len(rangeInt):
        ink = 2
        while ink < len(rangeInt):
            if rangeInt[index] * ink in rangeInt:
                rangeInt.remove(rangeInt[index] * ink)
            ink += 1
        index += 1
    rangeInt.insert(0, 1)
    print(rangeInt)
    return rangeInt

printSimpleNumbers(100)
