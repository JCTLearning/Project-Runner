from tkinter import *
isOpen = True
x = True

"""This Script is the Basic logic for the GUI (It will obviously have
custom buttons and not be default buttons. Just created this to refer
to creating buttons. We aren't using Datalists. We'll be putting their
inputs into a .json file so we can call it back and average the numbers.
"""
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        
    def init_window(self):      
        self.master.title("Track Thingy")
        self.pack(fill=BOTH, expand=1)
        
        #Creating Buttons for the GUI
        addData = Button(self, text="Inputs", command=self.cstop)
        stopProcess = Button(self, text = "Are you done?", command=self.output)
        #Setting Position of Buttons on the geom.
        addData.place(x = 5, y=0)
        stopProcess.place(x = 450, y = 0)
    def cstop(self):
        """Minor error (Forever loops and you can't clikck the
        gui
        """
        x = False
        while(isOpen == True):
            self.runnerName = input("[Runner Name]: ")
            self.runnerTime = input("[Runner Time]: ")
            self.rTime = []
            self.rName = []
            self.rTime.append(self.runnerTime)
            self.rName.append(self.runnerName)
            print(self.rTime)
            print(self.rName)
    def output(self):
        if(x = False):
            isOpen == False
        

root = Tk()

#size of the window
root.geometry("500x500")

app = Window(root)
root.mainloop()  
