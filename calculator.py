num1 = float(input("Enter first number: "))
what_2_do = input("Enter what you want to do: ")
num2 = float(input("Enter second number: "))
if what_2_do == "+":
    result = num1 + num2
elif what_2_do == "-":
    result = num1 - num2
elif what_2_do == "*":
    result = num1 * num2
elif what_2_do == "/" :
    if num2 == 0:
        result = "Don't fool around, you can't do that"
    else:
        result = num1 / num2
else:
    result = "Don't fool around"
print(result)