from tkinter import *
from PIL import Image, ImageTk

pathX = 'images\mouseX.png'
pathO = 'images\mouseO.png'

player1 = 0
player2 = 0

l1 = ''
l2 = ''
l3 = ''
l4 = ''
l5 = ''
l6 = ''
l7 = ''
l8 = ''
l9 = ''


class Click():

    def __init__(self, lbl):
        self.lbl = lbl
        self.lbl.bind('<Button-1>', self.x)
        self.lbl.bind('<Button-3>', self.o)

    def start_game(event):
        global l1, l2, l3, l4, l5, l6, l7, l8, l9
        l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = ''

        lbl_txt.configure(text=' ')

        lebel1.configure(text='', bg='white')
        lebel1.grid(row=1, column=1)
        lebel1.bind(Click(lebel1))

        lebel2.configure(text='', bg='white')
        lebel2.grid(row=1, column=2)
        lebel2.bind(Click(lebel2))

        lebel3.configure(text='', bg='white')
        lebel3.grid(row=1, column=3)
        lebel3.bind(Click(lebel3))

        lebel4.configure(text='', bg='white')
        lebel4.grid(row=2, column=1)
        lebel4.bind(Click(lebel4))

        lebel5.configure(text='', bg='white')
        lebel5.grid(row=2, column=2)
        lebel5.bind(Click(lebel5))

        lebel6.configure(text='', bg='white')
        lebel6.grid(row=2, column=3)
        lebel6.bind(Click(lebel6))

        lebel7.configure(text='', bg='white')
        lebel7.grid(row=3, column=1)
        lebel7.bind(Click(lebel7))

        lebel8.configure(text='', bg='white')
        lebel8.grid(row=3, column=2, padx=5)
        lebel8.bind(Click(lebel8))

        lebel9.configure(text='', bg='white')
        lebel9.grid(row=3, column=3)
        lebel9.bind(Click(lebel9))

    def x(self, event):
        global l1, l2, l3, l4, l5, l6, l7, l8, l9

        self.lbl.configure(text='X', fg='blue')

        if self.lbl == lebel1:
            l1 = 'X'
        elif self.lbl == lebel2:
            l2 = 'X'
        elif self.lbl == lebel3:
            l3 = 'X'
        elif self.lbl == lebel4:
            l4 = 'X'
        elif self.lbl == lebel5:
            l5 = 'X'
        elif self.lbl == lebel6:
            l6 = 'X'
        elif self.lbl == lebel7:
            l7 = 'X'
        elif self.lbl == lebel8:
            l8 = 'X'
        elif self.lbl == lebel9:
            l9 = 'X'

        self.test()

    def o(self, event):
        global l1, l2, l3, l4, l5, l6, l7, l8, l9

        self.lbl.configure(text='O', fg='red')

        if self.lbl == lebel1:
            l1 = 'O'
        elif self.lbl == lebel2:
            l2 = 'O'
        elif self.lbl == lebel3:
            l3 = 'O'
        elif self.lbl == lebel4:
            l4 = 'O'
        elif self.lbl == lebel5:
            l5 = 'O'
        elif self.lbl == lebel6:
            l6 = 'O'
        elif self.lbl == lebel7:
            l7 = 'O'
        elif self.lbl == lebel8:
            l8 = 'O'
        elif self.lbl == lebel9:
            l9 = 'O'

        self.test()

    def test(self):
        global player1, player2, l1, l2, l3, l4, l5, l6, l7, l8, l9


        if l1 == l2 == l3 == 'X' or l1 == l2 == l3 == 'O':
            lebel1.configure(bg='green', fg='black')
            lebel2.configure(bg='green', fg='black')
            lebel3.configure(bg='green', fg='black')

            if l1 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel4.grid_remove()
                lebel5.grid_remove()
                lebel6.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel9.grid_remove()
            elif l1 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel4.grid_remove()
                lebel5.grid_remove()
                lebel6.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel9.grid_remove()

        elif l4 == l5 == l6 == 'X' or l4 == l5 == l6 == 'O':
            lebel4.configure(bg='green', fg='black')
            lebel5.configure(bg='green', fg='black')
            lebel6.configure(bg='green', fg='black')

            if l4 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel1.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel9.grid_remove()
            elif l4 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel1.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel9.grid_remove()

        elif l7 == l8 == l9 == 'X' or l7 == l8 == l9 == 'O':
            lebel7.configure(bg='green', fg='black')
            lebel8.configure(bg='green', fg='black')
            lebel9.configure(bg='green', fg='black')

            if l7 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel1.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel4.grid_remove()
                lebel5.grid_remove()
                lebel6.grid_remove()
            elif l7 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel1.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel4.grid_remove()
                lebel5.grid_remove()
                lebel6.grid_remove()

        elif l1 == l4 == l7 == 'X' or l1 == l4 == l7 == 'O':
            lebel1.configure(bg='green', fg='black')
            lebel4.configure(bg='green', fg='black')
            lebel7.configure(bg='green', fg='black')

            if l1 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel2.grid_remove()
                lebel5.grid_remove()
                lebel8.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()
            elif l1 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel2.grid_remove()
                lebel5.grid_remove()
                lebel8.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()

        elif l2 == l5 == l8 == 'X' or l2 == l5 == l8 == 'O':
            lebel2.configure(bg='green', fg='black')
            lebel5.configure(bg='green', fg='black')
            lebel8.configure(bg='green', fg='black')

            if l2 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()
            elif l2 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()

        elif l3 == l6 == l9 == 'X' or l3 == l6 == l9 == 'O':
            lebel3.configure(bg='green', fg='black')
            lebel6.configure(bg='green', fg='black')
            lebel9.configure(bg='green', fg='black')

            if l3 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel2.grid_remove()
                lebel5.grid_remove()
                lebel8.grid_remove()
            elif l3 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel2.grid_remove()
                lebel5.grid_remove()
                lebel8.grid_remove()

        elif l1 == l5 == l9 == 'X' or l1 == l5 == l9 == 'O':
            lebel1.configure(bg='green', fg='black')
            lebel5.configure(bg='green', fg='black')
            lebel9.configure(bg='green', fg='black')

            if l1 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()
            elif l1 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel4.grid_remove()
                lebel7.grid_remove()
                lebel8.grid_remove()
                lebel2.grid_remove()
                lebel3.grid_remove()
                lebel6.grid_remove()

        elif l3 == l5 == l7 == 'X' or l3 == l5 == l7 == 'O':
            lebel3.configure(bg='green', fg='black')
            lebel5.configure(bg='green', fg='black')
            lebel7.configure(bg='green', fg='black')

            if l3 == 'X':
                player1 += 1
                lbl_pl_1.configure(text=str(player1))
                lbl_txt.configure(text='Выйграл - X', fg='white')
                lebel2.grid_remove()
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()
                lebel8.grid_remove()
            elif l3 == 'O':
                player2 += 1
                lbl_pl_2.configure(text=str(player2))
                lbl_txt.configure(text='Выйграл - O', fg='white')
                lebel2.grid_remove()
                lebel1.grid_remove()
                lebel4.grid_remove()
                lebel6.grid_remove()
                lebel9.grid_remove()
                lebel8.grid_remove()

        elif len(l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9) == 9:
            lbl_txt.configure(text='Ничья!', fg='white')
            lebel1.grid_remove()
            lebel2.grid_remove()
            lebel3.grid_remove()
            lebel4.grid_remove()
            lebel5.grid_remove()
            lebel6.grid_remove()
            lebel7.grid_remove()
            lebel8.grid_remove()
            lebel9.grid_remove()


root = Tk()
root.resizable(width=False, height=False)
root.configure(bg='black')

imgX = ImageTk.PhotoImage(Image.open(pathX))
imgO = ImageTk.PhotoImage(Image.open(pathO))

btn = Button(root, text='Начать Игру')
btn.grid(row=0, column=0, columnspan=5, padx=5, pady=3, sticky='ew')
btn.bind('<Button-1>', Click.start_game)

label_X = Label(root, bg='black', image=imgX)
label_X.grid(row=1, column=0, rowspan=3, padx=5, pady=3)
label_O = Label(root, bg='black', image=imgO)
label_O.grid(row=1, column=4, rowspan=3, padx=5, pady=3)

lbl_pl_1 = Label(root, relief=SUNKEN, text='0', font=10)
lbl_pl_1.grid(row=4, column=0, padx=5, pady=3, sticky='ew')
lbl_pl_2 = Label(root, relief=SUNKEN, text='0', font=10)
lbl_pl_2.grid(row=4, column=4, padx=5, pady=3, sticky='ew')

lbl_txt = Label(root, bg='black', font=10)
lbl_txt.grid(row=4, column=1, columnspan=3, sticky='ew')

lebel1 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel2 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel3 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel4 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel5 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel6 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel7 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel8 = Label(root, font=('Ubuntu', 20), width=4, height=2)
lebel9 = Label(root, font=('Ubuntu', 20), width=4, height=2)

root.mainloop()
