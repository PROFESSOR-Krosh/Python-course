'''
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
'''
a = [i for i in input().lower().split()]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key, value in d.items():
    print(key, value)