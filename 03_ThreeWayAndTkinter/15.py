#!/usr/bin/env python3

import tkinter as tk
import tkinter.messagebox as mb

import random
from datetime import datetime


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #set random seed
        random.seed(datetime.now())
        
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
        self.newButton = tk.Button(self.menuFrame, text='New',  command=self.newGame)
        
        self.newButton.grid(row=0, column=0)
        self.quitButton.grid(row=0, column=1)

    def createGameWidgets(self):
        for i in range(4):
            self.gameFrame.grid_rowconfigure(i, weight=2)
            self.gameFrame.grid_columnconfigure(i, weight=2)
        
        self.gameButtons = []
        
        def createLambda(fi,fj):
            return lambda: self.gameButtonPress(fi,fj)
        
        for i in range(4):
            self.gameButtons.append([])
            for j in range(4):
                if (i==3 and j==3):
                    self.gameButtons[i].append(None)
                else:
                    el = i*4+j+1
                    if (el)<=9:
                        s = ' '+str(el)
                    else:
                        s = str(el)
                    self.gameButtons[i].append(tk.Button(self.gameFrame, text=s, command=createLambda(i,j)))
                    
        self.gameMap = {}
        self.newGame()
                
    def newGame(self):
        for i in range(4):
            for j in range(4):
                self.gameMap[(i,j)]=(i,j)
        for i in range(4):
            for j in range(4):
                if (self.gameButtons[i][j]):
                    self.gameButtons[i][j].grid(row=i, column=j, sticky="nsew")
        self.availableMoves = [(3,2),(2,3)]
        self.shuffle()
        self.updatePositions()
        
    def checkWin(self):
        for i in range(4):
            for j in range(4):
                if (self.gameMap[(i,j)]!=(i,j)):
                    return False
        return True
        
    def win(self):
        mb.showinfo("You won!","Game will restart.")
        self.newGame()
        
    def gameButtonPress(self, i, j):
        mn = self.gameMap[(i,j)]
        m = mn[0]
        n = mn[1]
        if (self.doMove(m,n)):
            if (self.checkWin()):
                self.win()
        #print(self.gameMap)
         
    def shuffle(self):
        for _ in range(1000):
            rnd = random.choice(self.availableMoves)
            self.doMove(rnd[0],rnd[1])
        if (self.checkWin()):
            self.shuffle()
         
    def doMove(self, i, j):
        if (i,j) not in self.availableMoves:
            return False
        else:
            for key in self.gameMap:
                if (self.gameMap[key]==(i,j)):
                    self.gameMap[key]=self.gameMap[(3,3)]
            self.gameMap[(3,3)] = (i,j)
            self.availableMoves = []
            m = self.gameMap[(3,3)][0]
            n = self.gameMap[(3,3)][1]
            if (m-1)>=0:
                self.availableMoves.append((m-1,n))
            if (m+1)<=3:
                self.availableMoves.append((m+1,n))
            if (n-1)>=0:
                self.availableMoves.append((m,n-1))
            if (n+1)<=3:
                self.availableMoves.append((m,n+1)) 
            self.updatePositions()
            return True
            
    def updatePositions(self):
        for i in range(4):
            for j in range(4):
                if (self.gameButtons[i][j]):
                    m = self.gameMap[(i,j)]
                    self.gameButtons[i][j].grid(row=m[0], column=m[1], sticky="nsew")

app = Application()
app.master.title('Game15')
app.mainloop()
