# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input('Input a three-digit number: '))
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print (sum)