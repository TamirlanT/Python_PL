# Создать список
# Состоящих из кубов нечётных чисел от 1 до 1000
# Вычислить сумму тех чисел из этого списка
# сумма чисел которых Делится нацело на 7 number % 7 == 0
# Использовать только арифметические операции
# К каждому элементу списка добавить 17 и заново вычислить сумму чисел
# сумма фифр которых делится на 7

list = []
new_list = []
all_sum = 0

for i in range(1, 1000, 2):
    list.append(i**3)
print(list)


for i, v in enumerate(list):
    sum_digits = 0
    while v > 0:
        sum_digits += v % 10
        v //= 10
    if sum_digits % 7 == 0:
        all_sum +=list[i]
print(all_sum)

for m in list:
    new_list.append(m+17)

all_sum = 0
for i, v in enumerate(new_list):
    sum_digits = 0
    while v > 0:
        sum_digits += v % 10
        v //= 10
    if sum_digits % 7 == 0:
        all_sum += new_list[i]
print(all_sum)


list_of_cubes = []
all_sum = 0

for i in range(1, 1000, 2):
    list_of_cubes.append(i**3)

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val:
        sum_digits += val% 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]
    list_of_cubes[ind] += 17

print(all_sum)
