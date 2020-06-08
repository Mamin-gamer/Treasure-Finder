from tkinter import *
import random

class Map:
    def __init__(self, master):
        self.master = master
        rules = Label(self.master, text = 'find the bomb by pressing on the buttons with hint of direction', wraplength = 400, font = ('Courie', 14)).grid(columnspan = 3, row = 0)
        label1 = Label(self.master, text = 'Choose grid size', font = ('Courie', 30)).grid(columnspan = 3, row = 1, pady = 20, padx = 20)
        b = Button(self.master, text = '20x40(hard)', bd = 3, font = ('Courie', 14), command = lambda: self.draw(20, 40)).grid(column = 0, row = 2, pady = 20, padx = 10)
        b = Button(self.master, text = '14x30(medium)', bd = 3, font = ('Courie', 14), command = lambda: self.draw(15, 30)).grid(column = 1, row = 2, pady = 20, padx = 10)
        b = Button(self.master, text = '10x20(easy)', bd = 3, font = ('Courie', 14), command = lambda:self.draw(10, 20)).grid(column = 2, row = 2, pady = 20, padx = 10)

    def draw(self,rows, columns):
        self.play = True
        self.list = []
        self.master.withdraw()
        self.win = Toplevel(self.master)
        self.win.title('Click where you think the bomb is and try to grt the lowest number')
        self.win.resizable(False, False)
        self.win.protocol('WM_DELETE_WINDOW', on_closing)
        self.clicked_num = 0


        hidden_r = random.randrange(rows)
        hidden_c = random.randrange(columns)
        # print(hidden_r, hidden_c)
        for row in range(rows):
            for column in range(columns):
                distance = int(( (hidden_r - row)**2 + (hidden_c - column)**2 )  **0.5)
                self.draw_button(row, column, distance)


    def draw_button(self, row, column, distance):

        b = Button(self.win, text = '???',font = ('Courie', 10), fg = colour(row+column), command = lambda:self.button_action(distance,b))
        self.list.append(b)
        b.grid(column = column, row = row, padx = 1, pady = 1)

    def button_action(self, distance, button):

        button['text'] = distance
        button['fg'] = 'white'
        button['bg'] = 'blue'
        if distance == 0:
            self.play = False
        else:
            self.clicked_num+=1


        self.finish()




    def finish(self):
        if self.play == False:

            for b in self.list:
                b['state'] = 'disabled'

            temp = Toplevel(self.win)
            l = Label(temp, text = f'you found it in {self.clicked_num+1} attempts ', font = ('Courie',20)).grid(column = 1, row = 1, pady = 10, padx = 10)
            l1 = Button(temp, text = 'Do you want to play again?', font = ('Courie', 14), command = self.again).grid(columnspan = 3, row = 2, pady = 20, padx = 20)

            temp.protocol("WM_DELETE_WINDOW", on_closing)


    def again(self):
        main()
        print('aaa')


def colour(num):
    if num % 2 == 0:
        return 'red'
    return 'blue'

def on_closing():
    root.destroy()

def main():
    global root
    try:
        root.destroy()
        main()
    except:
        root = Tk()
        root.resizable(False, False)
        root.title('size guide')
        Map(root)

        root.mainloop()
if __name__ == '__main__':
    main()
