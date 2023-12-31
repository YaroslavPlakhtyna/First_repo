#Можливості пакетів math, cmath
#Для математичних обчислень у Python доданий пакет math. 
# Цей пакет містить ряд часто використовуваних математичних функцій та констант:

#Тригонометричні функції
# .sin / asin
# .cos / acos
# .tan / atan
# .hypot, обчислення відстані Евкліда між точками

#Перетворення кутів та радіанів:
# .degrees
# .radians

#Гіперболічні функції:
# .sinh / asinh
# .cosh / acosh
# .tanh / atanh

#Степеневі функції:
# .exp
# .pow (перетворить аргументи в float, на відміну від вбудованої pow)
# .sqrt
# .log2
# .log10
# .log логарифм із основою e, якщо основа не задана або із заданою основою.

#Константи:
# .pi
# .e
# .tau
# .inf, нескінченність
# .nan, не число


import math

math.sin(math.pi / 4)       # 0.7071067811865475
math.degrees(math.pi / 4)   # 45.0

#Якщо вам потрібна комплексна математика, то можна скористатися пакетом cmath. 
# Він надає той самий API, але вміє працювати з комплексними числами.

import cmath

cmath.sqrt(-4)  # 2j