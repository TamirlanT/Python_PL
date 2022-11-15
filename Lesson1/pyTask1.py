# Реализовать вывод информации о промежутке времени
# в зависимости от его прододжительности duration  в секундах.
# до: минуты <s> сек;
# до часа <m> мин, <s> сек;
# до суток <h> <m> <s>
# в остальных случаях <d> <h> <m> <s>

duration = int(input('Введите число: '))
d = duration // 3600 // 24
h = duration // 3600 - d * 24
m = duration // 60 % 60
s = duration % 60

print("days: ", d, "," " hours: ", h, ",", " minutes: ",
      m, ",", " seconds: ", s, ".", sep="")
# count = 60

# if duration < count:
#     print(f'{duration} секунд')
# elif duration >= count and duration < 3600:
#     m = duration // count
#     s = duration % count
#     print(f'{m} минут, {round(s, 2)} секунд')
# elif duration >= 3600 and duration < 86400:
#     if duration % count == 0:
#         m = duration / count
#         h = m / count
#         print (f'{h} часов')
#     else:
#         m = (duration // count) % count
#         h = (duration // count) // count
#         s = duration % count
#     print(f'{h} часов, {m} минут, {round(s, 2)} секунд')
# else:
#     m = (duration // count) % count
#     h = (duration // count) // count % 24
#     d = (duration // count) // count // 24
#     s = duration % count
# print(f'{d} дней, {h} часов, {m} минут, {round(s)} секунд')