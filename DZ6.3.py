num = int(input("Введите число: "))

while num > 9:
    result = 1

    while num > 0:
        digit = num % 10
        result *= digit
        num //= 10

    num = result

print(num)