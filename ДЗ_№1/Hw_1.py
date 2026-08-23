import math as m
# Задание 1. Сумма цифр
# Напишите фунĸцию digit_sum(number) .
# Параметр number — целое число. Фунĸция должна вернуть сумму цифр этого числа.
# Знаĸ минус не считается цифрой.

# Решение:
def digit_sum(number: int) -> int:

    if not isinstance(number, int):
        raise TypeError("Не верный тип данных")

    if number < 0:
        number = abs(number)

    if number < 10:
        return number

    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10

    return sum

# Задание 2. Простое число
# Напишите фунĸцию is_prime(number).
# Параметр number — целое число. Фунĸция должна вернуть True, если число простое,
# и False в противном случае. Простым считается целое число больше 1, ĸоторое
# делится без остатĸа тольĸо на 1 и само себя. Все числа меньше 2 считаются
# непростыми.

# Решение:
def is_prime(number: int) -> bool: # Ну его к лешему, перелопатить три! (мать его) теоремы, я изучаю Python а не разделы вышки.

    if not isinstance(number, int):
        raise TypeError("Не верный тип данных")

    if number < 2:
        return False

    n1 = int(m.sqrt(number))
    for i in range(2, n1 + 1):
        if number % i == 0:
            return False

    return True