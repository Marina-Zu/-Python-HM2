# Задайте список из n чисел, заполненный по формуле
# (1 + 1/n)**n и выведите на экран их сумму

n = int(input("Введите число > "))
my_list = []
total = 0
for i in range (1,n+1):
    my_list.append (round((1 + 1/i)**i))
    total = total + my_list[i-1]
print(my_list)
print(total)