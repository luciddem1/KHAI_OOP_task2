import math

def main():
    print("Практична робота №2 Степан Васильєв 312ст")  # Виведення інформації про практичну роботу та ім'я та групу студента
    task1()  
    newtask()  
    task2()  
    newtask()  
    task3()  

def newtask():  # Функція введення роздільної лінії та чекання введення користувача перед продовженням програми
    print("\n\n====================================================================================================================================================\n\n")
    input() 

def task1():
    print("=====Завдання 1=====\n")
    print("")
    x = float(input("Введіть координату x точки: "))
    y = float(input("Введіть координату y точки: "))

    if x > 0 and y > 0:
        result = 1
    elif x < 0 and y > 0:
        result = 2
    elif x < 0 and y < 0:
        result = 3
    elif x > 0 and y < 0:
        result = 4
    else:
        result = "Точка лежить на одній з координатних осей."

    print(f"Точка знаходиться в {result} координатній чверті.")


def task2():
    print("=====Завдання 2=====\n")
    print("∑ n=1 ->∞ = (n**3)/(2**(n+1))")

    series_sum = 0
    n = 0

    while True:
        n = int(input("Введіть кількість кроків: "))
        if n>0:
            break
        else:
            print(f"Число {n} менше нуля.")

    for i in range(1, n + 1):
        term = (i ** 3) / (2 ** (i + 1))
        series_sum += term

    print(f"∑ n=1 ->{n} = (n**3)/(2**(n+1)) = {series_sum}")



def task3():
    print("=====Завдання 3=====\n")
    print("∑ n=1 ->∞ = ((math.pi**n)*n**3)/(n!)")

    series_sum = 0
    n = 0

    while True:
        n = int(input("Введіть кількість кроків: "))
        if n>0:
            break
        else:
            print(f"Число {n} менше нуля.")

    for i in range(1, n + 1):
        term = ((math.pi**n)*n**3)/math.factorial(n)
        series_sum += term

    print(f"∑ n=1 ->{n} = ((math.pi**n)*n**3)/(n!) = {series_sum}")

main()