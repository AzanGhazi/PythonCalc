import math
import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('370x600')
        self.resizable(0,0)
        self.title('Calculator')
        self.value = 0.0
        self.expression = ""
        self.input_text = tk.StringVar()
        #Should contain things like application title, previous answer, secondary value
        self.frameWidgets = tk.Frame(self, height = 50, width=340, bg = "green")
        #self.frameWidgets.grid(row=0,column=0, padx=(5,5), pady=(0,5))
        self.frameWidgets.pack(side="top")
        self.topLabel = tk.Label(self.frameWidgets, text="Basic Calculator", font=('Helvatical bold',20))
        self.topLabel.grid(row=0, column=0)
        self.topLabel.pack(ipady=10)
        #self.input_field = tk.Entry(self.frameWidgets, textvariable = self.input_text, width = 50, bg = "#eee", bd =0, justify ="right")
        #self.input_field.grid(row=0, column=0)
        #self.input_field.pack(ipady=10)

        #Should incorperate things like Opperation being used, Main display, 
        self.frameCommandBar = tk.Frame(self, height = 120, width=340, bg = "blue")
        self.frameCommandBar.pack()

        self.input_field = tk.Entry(self.frameCommandBar, font=('arial', 18, 'bold'), textvariable = self.input_text, width = 30, bg = "white", bd =0, justify ="right")
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10, ipadx=10)
        
        #self.frameCommandBar.grid(row=1,column=0, padx=(5,5), pady=(5,5))
        #/Optional: Add frame that keeps a store of the last 5 calculations so we can go back. 
        self.frameMemoryBar = tk.Frame(self, height = 50, width=340, bg = "purple") 
        #self.frameMemoryBar.grid(row=2,column=0, padx=(5,5), pady=(5,5))
        #Command Grid : A series of buttons that will fill the screen, Contains all the useful commands. 
        self.frameCommandGrid = tk.Frame(self, height = 340, width=340, bg ="black")
        #self.frameCommandGrid.grid(row=3,column=0, padx=(5,5), pady=(5,0))
        self.frameCommandGrid.pack()
        
        #Row 1
        self.clear = tk.Button(self.frameCommandGrid, text="Clear", fg="black", width=38, height = 6, bd=0, bg="#FAEBD7", cursor="hand2").grid(row=0,column=0,columnspan=3,padx=1,pady=1)
        self.divide = tk.Button(self.frameCommandGrid, text="/", fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=0,column=3,padx=1,pady=1)
        #Row2
        
        self.button_7 = tk.Button(self.frameCommandGrid, text="7", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=0,padx=1,pady=1)
        self.button_8 = tk.Button(self.frameCommandGrid, text="8", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=1,padx=1,pady=1)
        self.button_9 = tk.Button(self.frameCommandGrid, text="9", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=2,padx=1,pady=1)
        self.button_multiply = tk.Button(self.frameCommandGrid, text="*", fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=1,column=3,padx=1,pady=1)
        #Row3

        self.button_4 = tk.Button(self.frameCommandGrid, text="4", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=0,padx=1,pady=1)
        self.button_5 = tk.Button(self.frameCommandGrid, text="5", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=1,padx=1,pady=1)
        self.button_6 = tk.Button(self.frameCommandGrid, text="6", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=2,padx=1,pady=1)
        self.button_minus = tk.Button(self.frameCommandGrid, text="-", fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=2,column=3,padx=1,pady=1)
        
        #Row4
        self.button_1 = tk.Button(self.frameCommandGrid, text="1", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=0,padx=1,pady=1)
        self.button_2 = tk.Button(self.frameCommandGrid, text="2", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=1,padx=1,pady=1)
        self.button_3 = tk.Button(self.frameCommandGrid, text="3", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=2,padx=1,pady=1)
        self.button_add = tk.Button(self.frameCommandGrid, text="+", fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=3,column=3,padx=1,pady=1)
        #Row5
        self.button_0 = tk.Button(self.frameCommandGrid, text="0", fg="black", width=25, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        self.button_dec = tk.Button(self.frameCommandGrid, text=".", fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=4,column=2,padx=1,pady=1)
        self.button_equals = tk.Button(self.frameCommandGrid, text="=", fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=4,column=3,padx=1,pady=1)
        
        
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




