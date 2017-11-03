from tkinter import *
global e
global runnerName
global runnerTime
#Made it here because too lazy honestly
def striptime(tstr):
    m, s = tstr.split(':')
    return int(m) * 60 + int(s)
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.windowC()
    def striptime(tstr):
        m, s = tstr.split(':')
        return int(m) * 60 + int(s)
    def manipulate(self):
        self.runnerName = self.e.get()
        self.runnerTime = self.e1.get()
        try:
            self.dab = striptime(self.runnerTime)
            print(self.dab)
        except:
            print("Something went wrong")
            self.root.destroy()
            self.root.quit()
            self.okay = Tk()
            self.okay.title("Error")
            self.T = Text(self.okay, height=2, width=30)
            self.T.insert(END, "Your input wasn't a valid input. Try again!")
            self.okay.mainloop()
            
            
            
    
    def windowC(self):
        #Input section for the GUI
        self.master.title("Runner Program")
        Label(self.master, text="Runner Name").grid(row = 0)
        Label(self.master, text ="Runner Time").grid(row=1)
        Button(self.master, text="Enter", command=self.manipulate).grid(row = 1, column = 2)
        self.e = Entry(self.master)
        self.e1 = Entry(self.master)

        
        self.e.grid(row=0, column = 1)
        self.e1.grid(row=1, column = 1)

        self.x = 0
        self.y = 5
            
        """def input(self):
            self.e.focus_set()
            self.e1.focus_set()

            self.dab = e.get()
            self.dab1 = e1.get()
            print(self.dab)
            print(self.dab1)"""
                
        
        #Output




        #Add bars to add excel files and manipulate this

    def printS(self):
        print("Hello!")


root = Tk()
root.geometry("1000x500")
app = Window(root)
root.mainloop()


