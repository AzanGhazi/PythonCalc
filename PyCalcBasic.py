import math
import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('350x600')
        self.title('Calculator')
        self.value = 0.0
        #Should contain things like application title, previous answer, secondary value
        self.frameWidgets = tk.Frame(self, height = 50, width=340, bg = "green")
        self.frameWidgets.grid(row=0,column=0, padx=(5,5), pady=(0,5))
        #Should incorperate things like Opperation being used, Main display, 
        self.frameCommandBar = tk.Frame(self, height = 120, width=340, bg = "blue") 
        self.frameCommandBar.grid(row=1,column=0, padx=(5,5), pady=(5,5))
        #/Optional: Add frame that keeps a store of the last 5 calculations so we can go back. 
        self.frameMemoryBar = tk.Frame(self, height = 50, width=340, bg = "purple") 
        self.frameMemoryBar.grid(row=2,column=0, padx=(5,5), pady=(5,5))
        #Command Grid : A series of buttons that will fill the screen, Contains all the useful commands. 
        self.frameCommandGrid = tk.Frame(self, height = 340, width=340, bg ="red")
        self.frameCommandGrid.grid(row=3,column=0, padx=(5,5), pady=(5,0m))
        
        ###declaration for Widgets

        #self.nameLabel = tk.Label(self.frameWidgets, height=60, width=1, bg = "light blue", text = "Basic Calculator")
        #self.nameLabel.pack(side = 'left')
        
        
        """

        self.grid()
        self.nameLabel = tk.Label(self, height = 5, width = 20, bg = "light blue", text = "Basic Calculator")
        #self.nameLabel.pack()
        self.nameLabel.grid(row=0, column=0)
        self.subLabel = tk.Label(self, height = 5, width = 20, bg= "light grey", text = self.value)
        #self.subLabel.pack()
        self.subLabel.grid(row=0,column=1)
        self.mainLabel = tk.Label(self, height = 5, width = 100, bg= "dark grey", text = self.value)
        #self.mainLabel.pack()
        self.mainLabel.grid(row=1)
        """

        #self.grid()


        

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()




