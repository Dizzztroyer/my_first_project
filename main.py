#1. Квадрат числа

number = int(input("Введите число: "))
print("Квадрат числа:", number ** 2)

#2. Среднее трех чисел

a1 = int(input("Введите первое число: "))
b1 = int(input("Введите второе число: "))
c1 = int(input("Введите третье число: "))
middle_num = (a1 + b1 + c1) / 3
print("Среднее тех чисел: ", middle_num)

#2.1. Второе решение(логичнее, как мне показалось) той же задачи,
#    помог gpt

numbers = list(map(int, input("Введите три числа через пробел: ").split()))
print("Среднее число: ", sum(numbers) / len(numbers))

#3. Перевести минуты в часы

minutes = int(input("Введите количество минут: "))
hours = minutes // 60
mins = minutes % 60
print(f"{hours} часов, {mins} минут")

#p.s. подумал что можно что-то сделать через if и list,
# чтобы корректно писалось "минут" и "минуты", но на
# английском таких проблем нет, там if <10 и все,
# остальное множественное число
# и то, вот пересмотрел и перечитал, не уверен теперь


#4. Расчет скидки

full_price = float(input("Введите цену: "))
discount_num = float(input("Введите скидку(%): "))

discount_price = full_price * discount_num / 100
final_price = full_price - discount_price
print(f"Цена со скидкой: {final_price}")


#5. Последняя цифра числа

number = int(input("Введите число: "))
last_num = number % 10
print(f"Последняя цифра: {last_num}")

#6. Периметр прямоугольника

a1 = float(input("Введите длину: "))
b1 = float(input("Введите ширину: "))
p = (a1 + b1) * 2
print(f"Периметр прямоугольника: {p}")

#7. Вывод числа в столбец

number = int(input("Введите 4-х значное число: "))
print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print(number % 10)
