# Напишите программу, которая принимает на вход два числа.
# Задайте список из N элементов, заполненных числаим из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях (не индексах)

a = int(input("Position one > "))
b = int(input("Position two > "))
n = int(input("Numbers of element > "))
my_list = []
result = 1
for i in range (-n,n+1):
    my_list.append (i)
print(my_list)
if 0 < a < n*2+2 and 0 < b < n*2+2:
    result = my_list[(a-1)] * my_list[(b-1)]
    print(result)
else:
    print("Non-correct value a or b")