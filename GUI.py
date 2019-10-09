from tkinter import *
from tkinter.messagebox import *
from datetime import datetime
from generate import finish_table
from sudoku import user_table

n = 1  # Число от 1 до 9
temp = 0
after_id = ''


class Numbers_1_9():

    def __init__(self, cell):
        self.cell = cell
        self.cell.bind('<Button-1>', self.n_in_cell)

    def n_in_cell(self, event):
        global n

        if n >= 10:
            n = 1

        self.cell.configure(text=n)
        n += 1


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
    clock_lbl.configure(text='00:00')
    root.after_cancel(after_id)


def brd_easy():  # лёгкая доска
    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'easy')  # Сгенерированная доска из модуля generate
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
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(text=str(nums))
                    break
                else:
                    num_brd += 1
                    continue
        c = -1


def brd_medium():  # средняя доска
    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'medium')  # Сгенерированная доска из модуля generate
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
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(text=str(nums))
                    break
                else:
                    num_brd += 1
                    continue
        c = -1


def brd_hard():  # сложная доска
    # Доска
    brd = {}  # Словарь с переменными(клетки на доске судоку)
    for n in range(1, 82):  # Генерация переменных
        n = 'label' + str(n)
        brd[n] = Label(root, width=2, font=('Ubuntu', 13))  # Присвоение каждой переменной виджета Label

    board = user_table(finish_table, 'hard')  # Сгенерированная доска из модуля generate
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
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3, pady=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, pady=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, pady=3)
                                brd[b].configure(text=str(nums))

                    else:
                        if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c, padx=3)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c, padx=3)
                                brd[b].configure(text=str(nums))

                        else:
                            if nums == 0:  # если nums == 0 выводим пустой виджет Label
                                brd[b].grid(row=r, column=c)
                                Numbers_1_9(brd[b])
                            else:
                                brd[b].grid(row=r, column=c)
                                brd[b].configure(text=str(nums))
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
root.configure(bg='black')

# Секундомер
clock_lbl = Label(root, width=8, font=('Ubuntu', 13), text='00:00')
clock_lbl.grid(row=0, column=3, columnspan=3, padx=3, pady=6)

clock_btn1 = Button(root, width=10, font=('Ubuntu', 9), text='Time-Start', command=start_clock)
clock_btn1.grid(row=0, column=0, columnspan=3, padx=3, pady=6)
clock_btn2 = Button(root, width=10, font=('Ubuntu', 9), text='Time-Stop', command=stop_clock)

# Кнопка проверки
btn = Button(root, width=10, font=('Ubuntu', 9), text='CHECK')
btn.grid(row=0, column=6, columnspan=3, padx=3, pady=6)

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

root.mainloop()
