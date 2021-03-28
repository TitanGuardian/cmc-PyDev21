import tkinter as tk
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master.grid()
        self.master.grid_rowconfigure(0, weight=20)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=2)
        self.master.grid_columnconfigure(1, weight=2)
        self.master.grid_columnconfigure(2, weight=2)
        
        #create field for exit and new game buttons
        self.editWindow = tk.Text(self.master, background="bisque")
        self.editWindow.grid(column=0, row=0, sticky="nsew")
        self.handleEdit()
        
        self.canvasWindow = tk.Canvas(self.master, background="pink")
        self.canvasWindow.grid(column=1, row=0, columnspan=3, sticky="nsew")
        self.handleGraph()
        
        self.syncEdit = tk.Button(self.master, text="SyncFromEdit", command=self.syncFromEdit)
        self.syncEdit.grid(column=0, row=1, sticky="nsew")
        self.syncGraph = tk.Button(self.master, text="SyncFromGraph", command=self.syncFromGraph)
        self.syncGraph.grid(column=1, row=1, sticky="nsew")
        self.buttonClear = tk.Button(self.master, text="Clear", command=self.Clear)
        self.buttonClear.grid(column=2, row=1, sticky="nsew")
       
    def syncFromEdit(self):
        self.canvasWindow.delete("all")
        self.ovalList=[]
        lines = self.editWindow.get('1.0', 'end-1c').split('\n')
        i = 1
        for line in lines:
            if line.strip() == "":
                i+=1
                continue
            #print(line.strip())
            search_res = re.match(r'\s*oval\s+\<\s*([\+\-]?\d\d*\.?\d*)\s\s*([\+\-]?\d\d*\.?\d*)\s\s*([\+\-]?\d\d*\.?\d*)\s\s*([\+\-]?\d\d*\.?\d*)\s*\>\s\s*([\+\-]?\d\d*\.?\d*)\s\s*([#\d\w]+)\s\s*([#\d\w]+)', line.strip() )
            #print(search_res)
            self.editWindow.tag_remove("Err", f"{i}.0", f"{i}.end")
            try:
                if not search_res:
                    raise Exception
                else:
                    ax = search_res.group(1)
                    ay = search_res.group(2)
                    bx = search_res.group(3)
                    by = search_res.group(4)
                    width = search_res.group(5)
                    border = search_res.group(6)
                    fill = search_res.group(7)
                    eval(f'self.ovalList.append(self.canvasWindow.create_oval(ax,ay,bx,by, width="{width}", outline="{border}", fill="{fill}"))')
            except:
                #print("Here")
                self.editWindow.tag_add("Err", f"{i}.0", f"{i}.end")
            i+=1
    
    def syncFromGraph(self):
        self.editWindow.delete('1.0', tk.END)
        for oval in self.ovalList:
            oval_string=""
            oval_string+="oval "
            oval_coords = self.canvasWindow.coords(oval)
            oval_string+="<"+str(oval_coords[0])+" "+str(oval_coords[1])+" "+str(oval_coords[2])+" "+str(oval_coords[3])+"> "
            oval_string+=str(self.canvasWindow.itemcget(oval,"width"))+" "
            oval_string+=str(self.canvasWindow.itemcget(oval,"outline"))+" "
            oval_string+=str(self.canvasWindow.itemcget(oval,"fill"))+"\n"
            self.editWindow.insert("end", oval_string)  

    def handleEdit(self):
        self.editWindow.tag_config("Err", background="pink")
    
    def handleGraph(self):
        self.ovalList=[]
        self.newoval = None
        self.canvasWindow.bind('<Button-1>', self.Click)
        self.canvasWindow.bind('<B1-Motion>', self.MotionDD)
        self.clickMode = 0
        self.overlap = None
        
    def Click(self, event):
        self.mousePosOnClick = [event.x, event.y]
        self.overlap = self.canvasWindow.find_overlapping(event.x, event.y, event.x, event.y)
        self.up = 1

    def MotionDD(self, event):
        if not (self.overlap):
            if self.up:
                self.ovalList.append(self.canvasWindow.create_oval(self.mousePosOnClick[0],self.mousePosOnClick[1], event.x, event.y, fill="Red"))
                self.up = 0
            else:
                self.canvasWindow.coords(self.ovalList[-1], self.mousePosOnClick[0], self.mousePosOnClick[1], event.x, event.y)   
        else:
            if (event.x < self.canvasWindow.winfo_width() and event.x > 0)  and (event.y < self.canvasWindow.winfo_height() and event.y > 0):
                self.canvasWindow.move(self.overlap[-1], event.x-self.mousePosOnClick[0], event.y-self.mousePosOnClick[1])
                self.mousePosOnClick = [event.x, event.y]
                
    
    def Clear(self):
        self.canvasWindow.delete("all")
        self.ovalList=[]

app = Application()
app.master.title('GraphRed')
app.mainloop()
