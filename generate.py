from random import sample

side = 3
square = side * side
nums = []
table = []
rows = []
cols = []
finish_table = []
# Случайное заполнение строки nums от 1 до 9
for num in sample(range(1, square + 1), square):
    nums.append(num)
# Генерация таблицы 9х9 со сдвигом в лево на side что исключает повторения, где num будет первой строкой
for r in range(square):
    t = []

    for c in range(square):
        t.append(nums[(side * (r % side) + r // side + c) % square])

    table.append(t)
# Случайное генерация номеров строк от 0 до 9 по 3-и числа(что бы сохранить не повторность при смешивании)
for i in sample(range(side), side):
    for r in sample(range(i * side, (i + 1) * side), side):
        rows.append(r)
# Случайное генерация номеров столбцов от 0 до 9 по 3-и числа(что бы сохранить не повторность при смешивании)
for i in sample(range(side), side):
    for c in sample(range(i * side, (i + 1) * side), side):
        cols.append(c)
# Перемешиваем с помощью сгенерированных ранее столбцов и строк
for r in rows:
    t = []

    for c in cols:
        t.append(table[r][c])

    finish_table.append(t)


if __name__ == '__main__':
    for line in finish_table:
        print(line)

    for l in range(9):
        print(sum(table[l]))
    print()

    for l in range(9):
        s = 0
        for i in range(9):
            s += finish_table[i][l]
        print(s)

