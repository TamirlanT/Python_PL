proc = ''
for n in range(1, 101):
    if n % 10 == 1 and n % 100 != 11:
        proc ='Процент'
    elif 1 < n % 10 < 5 and not 11 < n % 100 < 15:
        proc = 'Процента'
    else:
        proc = 'Процентов'
    print(f'{n}\t{proc}')