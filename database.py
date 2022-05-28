'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Sample Input:

a3b4c2e10b1

Sample Output:

aaabbbbcceeeeeeeeeeb
'''
inf = open('D:\\Desktop\\dataset_3363_2.txt', 'r')
s = inf.readline().strip()
inf.close()
res = ''
sym = 'A'
n = '0'
for i in range(len(s)):
	if s[i] >= 'A':
		sym = s[i]
		n = '0'
	elif s[i] < 'A' and n == '0':
		n = s[i]
	elif s[i] < 'A' and n != '0':
		n += s[i]
	if sym >= 'A' and int(n) > 0 and (i < len(s) - 1 and s[i + 1] >= 'A') or i == len(s) - 1:
		for y in range(int(n)):
			res += sym
print(res)