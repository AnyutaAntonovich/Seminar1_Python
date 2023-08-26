# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# number = int(input('Input a three-digit number: '))
# sum = 0
#
# while number > 0:
#     digit = number % 10
#     sum = sum + digit
#     number = number // 10
# print (sum)

n = 256

# Введите ваше решение ниже

# res = 0
# while n > 0:
#     digit = n % 10
#     res = res + digit
#     n = n // 10
# print(res)

n = int(n)

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
res = d1 + d2 + d3

print(res)