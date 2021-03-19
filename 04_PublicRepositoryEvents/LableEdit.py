
import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master = None):
        self.lableText = tk.StringVar("")
        super().__init__(master, takefocus=1
                               , textvariable=self.lableText
                               , font="TkFixedFont"
                               , anchor=(tk.W)
                               , relief = "sunken"
                               , highlightthickness=1
                        )
        self.createCursor()
        
    def createCursor(self):
        self.cursorPosition = 0
        self.cursor = tk.Frame(self, height=16, width=1, background="black")
        self.cursor.place(x=self.cursorPosition,y=1)
        self.bind('<Key>', self.eventHandler)
        self.bind('<Button-1>', self.mouseEvent)

    def eventHandler(self, event):
        coursorOffset = 0
        if event.keysym == "Left": 
            coursorOffset = -1
        elif event.keysym == "Right": 
            coursorOffset = 1
        elif event.keysym == "Home":
            self.cursorPosition = 0
        elif event.keysym == "End":
            self.cursorPosition = len(self.lableText.get())
        elif event.keysym == "BackSpace":
            if self.cursorPosition > 0:
                self.lableText.set(self.lableText.get()[:self.cursorPosition-1]
                                 +self.lableText.get()[self.cursorPosition:]
                                 )
                coursorOffset = -1
        elif event.char:
            self.lableText.set(self.lableText.get()[:self.cursorPosition]
                                +event.char
                                +self.lableText.get()[self.cursorPosition:]
                                )
            coursorOffset = 1
        
        #update cursor
        if (coursorOffset==1):
            if (self.cursorPosition != len(self.lableText.get())):
                self.cursorPosition += coursorOffset
        elif (coursorOffset==-1):
            if (self.cursorPosition != 0):
                self.cursorPosition += coursorOffset
        self.cursor.place(x=self.cursorPosition*8+1, y=1)
        
    def mouseEvent(self, event):
        self.focus_set()
        if (event.x//8<=len(self.lableText.get())): 
            self.cursorPosition = event.x//8
        else:
            self.cursorPosition = len(self.lableText.get())
        self.cursor.place(x=self.cursorPosition*8+1, y=1)

class Application(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        self.labelText = InputLabel(self) 
        self.labelText.grid(sticky="nsew")
        self.buttonQuit = tk.Button(self, text = "Quit", command = self.master.quit)
        self.buttonQuit.grid(row=1)
        
        
app = Application()
app.mainloop()
