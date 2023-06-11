# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Input the length of the chocolate bar: '))
m = int(input('Input the width of the chocolate bar: '))
k = int(input('How many slices do you want to break off? '))

if k % m == 0 or k % n == 0 and m * n > k:
    print('Yes')
else:
    print('No')