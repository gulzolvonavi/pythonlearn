import random


value_1 = random.randint(0,9)
value_2 = random.randint(0,9)

oper = input()

if oper == "+":
    print(value_1, " + ", value_2, " = ", value_1+value_2)

elif oper == "-":
    print(value_1, " - ", value_2, " = ", value_1-value_2)

elif oper == "*":
    print(value_1, " * ", value_2, " = ", value_1*value_2)

elif oper == "/":
    print(value_1, " / ", value_2, " = ", value_1/value_2)



else:
    print("Введите нормальный знак")

