# Завдання 2

# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.
#
# mainword = input("Введіть слово: ")
#
# def main():
#     if mainword == mainword[::-1]:
#         return True
#     else:
#         return False
#
# if main():
#     print("Слово є паліндромом")
# else:
#     print("Слово не є паліндромом")

#Завдання 2
#Створіть програму, яка перевіряє, чи є паліндромом введена фраза.
#def stairs(n):
 #   if n == 1:
  #      return 1
  #  if n == 2:
    #    return 2

  #  a, b = 1, 2

  #  for _ in range(3, n + 1):
       # a, b = b, a + b

  #  return b


#n = int(input("Введите номер ступеньки: "))
#print(stairs(n))
# task 4
# Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.
#def sum_range(a, b):
   # if a == b:      # базовый случай
        #return a
    #return a + sum_range(a + 1, b)  # рекурсивный вызов


#a = int(input("Введіть початок проміжку: "))
#b = int(input("Введіть кінець проміжку: "))

#print("Сума чисел =", sum_range(a, b))

# Task 5
import math
def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_rezult(a, b, c):
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)

        elif D == 0:
            x1 = -b / (2 * a)
            x2 = None

        else:
            x1 = None
            x2 = None

        return x1, x2

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

print(quadratic_equation(a, b, c))