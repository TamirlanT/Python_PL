# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for i in list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            new_list.append(f"'{int(i):02}'")
        else:
            new_list.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        new_list.append(i)
print(new_list)
print(" ".join(new_list))
print("\n")

# Сложный вариант

for i, v in enumerate(list):
    if v.isdigit():
        new_list[i] = f'"{int(v):02}"'
    elif v[1:].isdigit():
        new_list[i] = f'"{v[0]}{int(v[1:]):02}"'

print(new_list)
print(" ".join(new_list))
