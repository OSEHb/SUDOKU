from tkinter import *
from datetime import datetime
from generate import finish_table
from sudoku import user_table

n = 1  # Число от 1 до 9
temp = 0
after_id = ''
test_board = []  # Доска для проверки решения


class Numbers_1_9():  # Класс для вывода цифр в клетке доски

    def __init__(self, cell, rw, cl):
        self.rw = rw  # Строка в доске
        self.cl = cl  # Столбец в доске
        self.cell = cell  # Пустая клетка
        self.cell.bind('<Button-1>', self.n_in_cell)
        self.cell.bind('<Button-3>', self.del_n_in_cell)

    def n_in_cell(self, event):
        global n, test_board

        if n >= 10:
            n = 1

        self.cell.configure(fg='#085e00', text=n)
        test_board[self.rw - 1][self.cl] = n
        n += 1

    def del_n_in_cell(self, event):
        self.cell.configure(fg='#085e00', text=' ')
        test_board[self.rw - 1][self.cl] = 0


def start_clock():
    global temp, after_id

    clock_btn1.grid_forget()  # Удаляем кнопку СТАРТ
    clock_btn2.grid(row=0, column=0, columnspan=3, padx=3, pady=6)  # Добавляем кнопку СТОП

    after_id = root.after(1000, start_clock)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    clock_lbl.configure(text=str(f_temp))
    temp += 1


def stop_clock():
    global temp

    clock_btn2.grid_forget()  # Удаляем кнопку СТОП
    clock_btn1.grid(row=0, column=0, columnspan=3, padx=3, pady=6)  # Добавляем кнопку СТАРТ
    # Обнуляю секундомер
    temp = 0
    root.after_cancel(after_id)


def test(event):
    row = 0
    col = 0

    for i in test_board:
        row += 1
        result = sum(i)

        if result != 45:
            return status_bar.configure(text='Wrong decision! row: ' + str(row), fg='red')

    for j in range(0, 9):
        col += 1
        result = test_board[0][j] + test_board[1][j] + test_board[2][j] + test_board[3][j] + test_board[4][j] + \
            test_board[5][j] + test_board[6][j] + test_board[7][j] + test_board[8][j]

        if result != 45:
            return status_bar.configure(text='Wrong decision! column: ' + str(col), fg='red')

    return status_bar.configure(text="Congratulations, you're good!", fg='green')


def brd_easy():  # лёгкая доска
    global test_board

    status_bar.configure(text='')

    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'easy')  # Сгенерированная доска из модуля generate
    test_board = board
    r = 0  # строка в GUI
    c = -1  # столбец в GUI
    brd_index = 0  # индекс для пропуска уже внесённых переменных из brd

    for row in board:  # строка из полученой таблицы
        r += 1

        for nums in row:  # значение из полученой таблицы
            c += 1
            num_brd = 1  # номер переменной из brd
            brd_index += 1

            for b in brd:  # переменная из словоря brd(наша визуализация доски)
                if num_brd == brd_index:
                    # if и else дают разницу в отступах между квадратами
                    if r == 1 or r == 3 or r == 4 or r == 6 or r == 7 or r == 9:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(bg='#c3c8db', text=str(nums))
                    break
                else:
                    num_brd += 1
                    continue
        c = -1


def brd_medium():  # средняя доска
    global test_board

    status_bar.configure(text='')

    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'medium')  # Сгенерированная доска из модуля generate
    test_board = board
    r = 0  # строка в GUI
    c = -1  # столбец в GUI
    brd_index = 0  # индекс для пропуска уже внесённых переменных из brd

    for row in board:  # строка из полученой таблицы
        r += 1

        for nums in row:  # значение из полученой таблицы
            c += 1
            num_brd = 1  # номер переменной из brd
            brd_index += 1

            for b in brd:  # переменная из словоря brd(наша визуализация доски)
                if num_brd == brd_index:
                    # if и else дают разницу в отступах между квадратами
                    if r == 1 or r == 3 or r == 4 or r == 6 or r == 7 or r == 9:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(bg='#c3c8db', text=str(nums))
                    break
                else:
                    num_brd += 1
                    continue
        c = -1


def brd_hard():  # сложная доска
    global test_board

    status_bar.configure(text='')

    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'hard')  # Сгенерированная доска из модуля generate
    test_board = board
    r = 0  # строка в GUI
    c = -1  # столбец в GUI
    brd_index = 0  # индекс для пропуска уже внесённых переменных из brd

    for row in board:  # строка из полученой таблицы
        r += 1

        for nums in row:  # значение из полученой таблицы
            c += 1
            num_brd = 1  # номер переменной из brd
            brd_index += 1

            for b in brd:  # переменная из словоря brd(наша визуализация доски)
                if num_brd == brd_index:
                    # if и else дают разницу в отступах между квадратами
                    if r == 1 or r == 3 or r == 4 or r == 6 or r == 7 or r == 9:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(bg='#c3c8db', text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b], r, c)
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(bg='#c3c8db', text=str(nums))
                    break
                else:
                    num_brd += 1
                    continue
        c = -1


def exit_app():  # Выход из судоку
    root.destroy()


# GUI для судоку
root = Tk()
root.title('SUDOKU')
root.resizable(width=False, height=False)
root.configure(bg='#1b1e29')

# Секундомер
clock_lbl = Label(root, width=8, font=('Ubuntu', 13), text='00:00', bg='#1b1e29', fg='white')
clock_lbl.grid(row=0, column=3, columnspan=3, padx=3, pady=6)

clock_btn1 = Button(root, width=10, font=('Ubuntu', 9), text='Time-Start', command=start_clock)
clock_btn1.grid(row=0, column=0, columnspan=3, padx=3, pady=6)
clock_btn2 = Button(root, width=10, font=('Ubuntu', 9), text='Time-Stop', command=stop_clock)

# Кнопка проверки
btn = Button(root, width=10, font=('Ubuntu', 9), text='CHECK')
btn.grid(row=0, column=6, columnspan=3, padx=3, pady=6)
btn.bind('<Button-1>', test)

# Статус бар
status_bar = Label(root, relief=SUNKEN, width=25, text='For the start: File - New Game')
# relief-определяет тип рамки элемента
status_bar.grid(row=10, columnspan=9, padx=3, pady=6)

# Главное меню окна, с выбором сложности
main_menu = Menu(root)
root.configure(menu=main_menu)

item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=item)

difficulty = Menu(item, tearoff=0)
item.add_cascade(label='New Game', menu=difficulty)
difficulty.add_radiobutton(label='Easy', command=brd_easy)
difficulty.add_radiobutton(label='Medium', command=brd_medium)
difficulty.add_radiobutton(label='Hard', command=brd_hard)
# Меню выхода с разделителем
item.add_separator()
item.add_command(label='Exit', command=exit_app)

root.iconbitmap('img\icon.ico')
root.mainloop()


if __name__ == '__main__':
    for abc in test_board:
        print(abc)
