# EASY: Задача 1
# Решение 1
print("EASY 1, Решение 1:")
number = int(input("Введите целое число и нажимите Enter "))
while number > 0:
    print(number % 10)
    number = number // 10


# Решение 2 (не мое)
print("EASY 1, Решение 2:")
for s in input():
    print(s)

# EASY Задача 2:
print("EASY 2:")
a = int(input("Введите первую переменную и нажимите Enter "))
b = int(input("Введите вторую переменную и нажимите Enter "))
c = a
a = b
b = c
print("переменная a =", a)
print("переменная b =", b)

# EASY Задача 3
print("EASY 3:")
a = int(input("Введите ваш возраст "))
if a >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

# NORMAL Задача 1
print("Normal 1:")
number1 = int(input("Введите целое число и нажимите Enter "))
mx = 0
while number1 > 0:
    c = number1 % 10
    if c >= mx:
        mx = c
    number1 //= 10
print(mx)

# NORMAL Задача 2
print("NORMAL 2:")
a = int(input("Введите первую переменную и нажимите Enter "))
b = int(input("Введите вторую переменную и нажимите Enter "))
a = a + b
b = a - b
a = a - b
print("переменная a =", a)
print("переменная b =", b)

# NORMAL Задача 3
print("NORMAL 3:")
a = int(input("Введите первый коэффициент уравнения ax² + bx + c = 0 и нажимите Enter "))
b = int(input("Введите второй коэффициент уравнения ax² + bx + c = 0 и нажимите Enter "))
c = int(input("Введите третий коэффициент уравнения ax² + bx + c = 0 и нажимите Enter "))
print(a, "*x² +", b, "*x +", c, "= 0")
D = b ** 2 - 4 * a * c
if D > 0:
    print("No roots")
else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("x1=", x1, "x2=", x2)

# HARD Задача 1
print("HARD 1:")
number2 = int(input("Введите число и нажимите Enter "))
if number2 > 1:
    A = int(number2 // 1)
    if number2 != A:
        print(number2, "Это не простое число")
    else:
            print(number2, "Это простое число")
else:
    print(number2, "Это не простое число")

# HARD Задача 2
print("HARD 2:")
number1 = 1
number2 = 1
n = int(input("Введите номер элемента ряда Фибоначчи: "))
for i in range(n-1):
    fib_sum = number1 + number2
    number1 = number2
    number2 = fib_sum
print(number2)

# HARD Задача 3
print("HARD 3:")
a = int(input("Введите колличество строк и нажимите Enter "))
b = int(input("Введите количество триплетов и нажимите Enter "))
for i in range(a):
    s = str("AAABBB")
    print(s*b)