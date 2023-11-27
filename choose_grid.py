from tkinter import *

from game import Game

class ChooseGameMode():
    root = Tk()
    root.title('SAPPER')
    root.geometry('400x400')
    screen_size = (root.winfo_screenwidth(), root.winfo_screenheight())
    label_text = StringVar()
    label_text.set(f"Own grid size (must be between {screen_size[0] // 60} and {screen_size[1] // 60})")
    mainframe = Frame(root, width=200, height=200, bg='white')
    mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    label = Label(mainframe, textvariable=label_text, relief=RAISED)
    label.place(relx=0.15, rely=0.63, relwidth=0.7, relheight=0.05)

    def init_ui(self):

        btn1 = Button(self.mainframe, text='11x11', command=lambda: self.initialize_game([11, 11]))
        btn1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

        btn2 = Button(self.mainframe, text='12x12', command=lambda: self.initialize_game([12, 12]))
        btn2.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)

        btn3 = Button(self.mainframe, text='13x13', command=lambda: self.initialize_game([13, 13]))
        btn3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        grid_size_x = Entry(self.mainframe, bg='white', font=30)
        grid_size_x.place(relx=0.15, rely=0.7, relwidth=0.20, relheight=0.05)

        grid_size_y = Entry(self.mainframe, bg='white', font=30)
        grid_size_y.place(relx=0.65, rely=0.7, relwidth=0.20, relheight=0.05)

        btn = Button(self.mainframe, text='start', command=lambda: self.initialize_game([grid_size_x.get(), grid_size_y.get()]))
        btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.05)

        info = Label(self.mainframe, text='SAPPER', bg='#ffb700', font=40)
        info.pack()

        self.root.mainloop()

    def initialize_game(self, grid_size):
        try:
            grid_size[0] = int(grid_size[0])
            grid_size[1] = int(grid_size[1])
        except ValueError:
            self.label_text.set("values x y must be digit")
            return
        if ((int(grid_size[0])) * 60) > self.screen_size[0] or ((int(grid_size[1])) * 60) > self.screen_size[1]:
            self.label_text.set("Grid is bigger than size of your screen")
            return

        self.root.destroy()
        Game(grid_size).start_game()