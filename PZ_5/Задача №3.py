# Написать программу, подсчитывающую количество цифр числа, используя для
# этого функцию.

x = int(input("Введите число: "))
def count_digits(x):

    if x == 0:
        return 1

    # c отрицательными числами
    # x = abs(x)
    digit = 0
    while x > 0:
        x //= 10  # Делю число на 10 и отбрасываю остаток
        digit += 1
    return digit

digit = count_digits(x)
print(f"Количество цифр в числе {x}: {digit}")