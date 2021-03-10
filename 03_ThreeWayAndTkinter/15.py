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
        for i in range(4):
            self.gameFrame.grid_rowconfigure(i, weight=2)
            self.gameFrame.grid_columnconfigure(i, weight=2)
        
        self.gameButtons = []
        
        def create_lambda(fi,fj):
            return lambda: self.game_button_press(fi,fj)
        
        for i in range(4):
            self.gameButtons.append([])
            for j in range(4):
                if (i==3 and j==3):
                    self.gameButtons[i].append(None)
                else:    
                    self.gameButtons[i].append(tk.Button(self.gameFrame, text=str(i*4+j+1), command=create_lambda(i,j)))    
        for i in range(4):
            for j in range(4):
                if (self.gameButtons[i][j]):
                    self.gameButtons[i][j].grid(row=i, column=j, sticky="nsew")
        
        self.gameMap = {}
        for i in range(4):
            for j in range(4):
            self.gameMap[(i,j)]=(i,j)
                
    def new_game(self):
        print(self.gameButtons)
        
    def win(self):
        pass #TODO
        
    def game_button_press(self, i, j):
        print(i,j)

app = Application()
app.master.title('Sample application')
app.mainloop()
