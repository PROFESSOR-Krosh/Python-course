'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
matrix = []
row = 0
column = 0
while True:
    a = input()
    if a == "end":
        break
    else:
        b = [int(i) for i in a.split()]
        row = len(b)
        matrix.append(b)
        column += 1

newmatrix = [[0 for i in range(row)] for j in range(column)]
for i in range(column):
    for j in range(row):
        for dj in -1, 1:
            if j == 0 and dj == -1:
                newmatrix[i][j] += matrix[i][row - 1]
            elif j == row - 1 and dj == 1:
                newmatrix[i][j] += matrix[i][0]
            else:
                newmatrix[i][j] += matrix[i][j + dj]
        for di in -1, 1:
            if i == 0 and di == -1:
                newmatrix[i][j] += matrix[column - 1][j]
            elif i == column - 1 and di == 1:
                newmatrix[i][j] += matrix[0][j]
            else:
                newmatrix[i][j] += matrix[i + di][j]

for i in newmatrix:
    for j in i:
        print(j, end=' ')
    print()
