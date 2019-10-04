from tkinter import *
from generate import finish_table
from sudoku import user_table


class Board:
    # Принимаем сложность уровня
    def __init__(self, deff):
        self.deff = deff

    # Выводим таблицу в зависимости от сложности
    def brd(self):
        board = user_table(finish_table, self.deff)
        r = 0  # строка
        c = -1  # столбец

        for row in board:
            r += 1

            for nums in row:
                c += 1
                # if и else дают разницу в отступах между квадратами
                if r == 1 or r == 3 or r == 4 or r == 6 or r == 7 or r == 9:
                    if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                        label = Label(root, width=2, font=10, text=str(nums))
                        label.grid(row=r, column=c, padx=3, pady=3)
                    else:
                        label = Label(root, width=2, font=10, text=str(nums))
                        label.grid(row=r, column=c, pady=3)
                else:
                    if c == 0 or c == 2 or c == 3 or c == 5 or c == 6 or c == 8:
                        label = Label(root, width=2, font=10, text=str(nums))
                        label.grid(row=r, column=c, padx=3)
                    else:
                        label = Label(root, width=2, font=10, text=str(nums))
                        label.grid(row=r, column=c)
            c = -1


def exit_app():
    root.destroy()


# Oкно для судоку
root = Tk()
root.title('SUDOKU')
root.resizable(width=False, height=False)
root.configure(bg='black')
# Секундомер
clock_lbl = Label(root, width=8, font=('Ubuntu', 13), text='00:00')
clock_lbl.grid(row=0, column=3, columnspan=3, padx=3, pady=6)
# Кнопка проверки
btn1 = Button(root, width=10, font=('Ubuntu', 9), text='CHECK')
btn1.grid(row=0, column=6, columnspan=3, padx=3, pady=6)
# Главное меню окна, с выбором сложности
main_menu = Menu(root)
root.configure(menu=main_menu)

item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=item)

difficulty = Menu(item, tearoff=0)
item.add_cascade(label='New Game', menu=difficulty)
difficulty.add_radiobutton(label='Easy', command=Board('easy').brd)
difficulty.add_radiobutton(label='Medium', command=Board('medium').brd)
difficulty.add_radiobutton(label='Hard', command=Board('hard').brd)
# Меню выхода с разделителем
item.add_separator()
item.add_command(label='Exit', command=exit_app)

root.mainloop()
