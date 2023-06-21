from tkinter import *
from tkinter import messagebox
import random

cells = []
cell = []
player = 'X'
window = Tk()
window.title("Крестики-нолики")
window.minsize(width=250, height=250)

#Эти строки инициализируют переменные. cells и cell - это многомерные списки для хранения каждой ячейки игровой доски, player - это переменная для отслеживания текущего игрока (X или O), а window - это основное окно приложения, которое устанавливает заголовок и размеры.

def check_win(): 
    for i in range(0, 3):
        if (cell[i*3]['text'] == cell[i*3+1]['text'] == cell[i*3+2]['text'] == player or
            cell[i]['text'] == cell[i+3]['text'] == cell[i+6]['text'] == player):
            return True
    if (cell[0]['text'] == cell[4]['text'] == cell[8]['text'] == player or
        cell[2]['text'] == cell[4]['text'] == cell[6]['text'] == player):
        return True
    return False

#Эта функция проверяет, выиграл ли какой-либо игрок, рассматривая все возможные выигрышные комбинации из трех ячеек, связанных последовательно на доске. Сначала она проверяет ряды и столбцы, а затем обе диагонали. Функция возвращает True, если текущий игрок выиграл, False в противном случае.


def play(n):
    global player
    if cell[n]['text'] == "":
        cell[n].config(text=player)
        if check_win(): 
            messagebox.showinfo('Победитель!', f'Игрок {player} выиграл!')
            window.destroy()
            return
        elif all(cell[i]['text'] for i in range(0, 9)):
            messagebox.showinfo('Ничья', 'Никто не выиграл.')
            window.destroy()
            return
        player = 'O' if player == 'X' else 'X'
        if player == 'O':
            ai_play()

#Д

def ai_play():
    empty_cells = [i for i in range(len(cell)) if not cell[i]['text']]
    if empty_cells:
        empty_cell = random.choice(empty_cells)
        play(empty_cell)


for i in range(3):
    cells.append(Frame(window))
    cells[i].pack(expand=YES, fill=BOTH)
    for j in range(3):
        cell.append(
            Button(cells[i], text='', font=('monospace', 24, 'bold'), width=3, height=2))
        cell[i * 3 + j].config(command=lambda n=i * 3 + j: play(n))
        cell[i * 3 + j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
      
window.mainloop()
