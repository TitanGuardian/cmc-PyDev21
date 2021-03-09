#!/usr/bin/env python3

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #game frame will fill all free space
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        #create field for exit and new game buttons
        self.menuFrame = tk.Frame(self.master, background="bisque")
        self.menuFrame.grid(column=0, row=0, sticky="nsew")
        self.createMenuWidgets()
        
        self.gameFrame = tk.Frame(self.master, background="pink")
        self.gameFrame.grid(column=0, row=1, sticky="nsew")
        self.createGameWidgets()
        

    def createMenuWidgets(self):
        self.menuFrame.grid_columnconfigure(0, weight=1)
        self.menuFrame.grid_columnconfigure(1, weight=1)
        self.quitButton = tk.Button(self.menuFrame, text='Quit', command=self.quit)
        self.newButton = tk.Button(self.menuFrame, text='New',  command=self.new_game)
        
        self.newButton.grid(row=0, column=0)
        self.quitButton.grid(row=0, column=1)

    def createGameWidgets(self):
        self.gameFrame.grid_rowconfigure(0, weight=2)
        self.gameFrame.grid_rowconfigure(1, weight=2)
        self.gameFrame.grid_columnconfigure(0, weight=2)
        self.gameFrame.grid_columnconfigure(1, weight=2)
        
        self.gameButton0 = tk.Button(self.gameFrame, text='GAME0')
        self.gameButton1 = tk.Button(self.gameFrame, text='GAME1')
        self.gameButton2 = tk.Button(self.gameFrame, text='GAME2')
        self.gameButton3 = tk.Button(self.gameFrame, text='GAME3')
        
        self.gameButton0.grid(row=0, column=0, sticky="nsew")
        self.gameButton1.grid(row=0, column=1, sticky="nsew")
        self.gameButton2.grid(row=1, column=0, sticky="nsew")
        self.gameButton3.grid(row=1, column=1, sticky="nsew")
        

    def new_game(self):
        pass #TODO
        
    def win(self):
        pass #TODO
        

app = Application()
app.master.title('Sample application')
app.mainloop()
