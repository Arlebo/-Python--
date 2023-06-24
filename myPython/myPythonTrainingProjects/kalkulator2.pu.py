# калькулятор

from colorama import Fore, Back, Style
from colorama import init
init()

a = float(input(Fore.GREEN + "Введи первое число:  "))
what = input(Fore.GREEN + "Что делаем? (+, -, *, /): ")
b = float(input(Fore.GREEN + "Введи второе число:  "))
if what == "+":
    c = a + b
    print(Fore.BLUE + "Результат: " + str(c))
elif what == "-":
    c = a - b
    print(Fore.BLUE + "Результат: " + str(c))
elif what == "*":
    c = a * b
    print(Fore.BLUE + "Результат: " + str(c))
elif what == "/":
    c = a / b
    print(Fore.BLUE + "Результат: " + str(c))
else:
    print(Fore.RED + "Выбрана неверная операция!")
    
input()
