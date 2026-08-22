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