# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
#   thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*args):
    dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in dict:
            dict[letter] += [i]
        else:
            dict[letter] = [i]
    return dict


print(thesaurus('Иван', "Мария", "Илья", "Петр", 'Ильдус'))


def thesauruh(*args):
    main_list = {}
    for i in sorted(args):
        if i[0] not in main_list:
            main_list[i[0]] = list(filter(lambda el: el.startswith(i[:1]), args))
    print(main_list)


thesauruh('Лариса', "Альберт", "Локоть", "Дмитрий", "Ильдус")


def thesausus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append((s_n))
    return s_n_sort

print(thesausus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельвева",
                        "Юнона Ветрякова"))
