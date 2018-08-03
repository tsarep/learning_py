# Реализуйте при помощи python и библиотеки math (import math) формулу длины окружности через площадь круга. L= 2√(s*π)

import math
print('Введите площадь круга:')
s = int(input())
l = 2 * math.sqrt(s * math.pi)
print('Длина окружности ', l)
