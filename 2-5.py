# Реализуйте алгоритм перемешивания списка.

n = int(input("Введите длину списка > "))
my_list = []
out_list = []
for i in range (n):
    my_list.append (i)
print(my_list)
j = 0
if j < len(my_list):
    for l in range(3):
        k = n
        while k >= 3:
            k = k - 3
            out_list.append(my_list[k])
            j += 1
        n = n + 1
print(out_list)