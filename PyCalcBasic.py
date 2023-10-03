import math
import tkinter as tk


class Calculator(tk.Tk):
    

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_back(self):
        try:
            self.expression = self.expression.rstrip(self.expression[-1])
            self.input_text.set(self.expression)
        except IndexError:
            pass

    def btn_clear(self):
        self.expression =""
        self.input_text.set("")

    def btn_equal(self):
        try: 
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except SyntaxError:
            pass

    
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

        self.frameWidgets.pack(side="top")
        self.topLabel = tk.Label(self.frameWidgets, text="Basic Calculator", font=('Helvatical bold',20))
        self.topLabel.grid(row=0, column=0)
        self.topLabel.pack(ipady=10)


        #Should incorperate things like Opperation being used, Main display, 
        self.frameCommandBar = tk.Frame(self, height = 120, width=340, bg = "blue")
        self.frameCommandBar.pack()

        self.input_field = tk.Entry(self.frameCommandBar, font=('arial', 18, 'bold'), textvariable = self.input_text, width = 30, bg = "white", bd =0, justify ="right")
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10, ipadx=10)
        

        #/Optional: Add frame that keeps a store of the last 5 calculations so we can go back. 

        #Command Grid : A series of buttons that will fill the screen, Contains all the useful commands. 
        self.frameCommandGrid = tk.Frame(self, height = 340, width=340, bg ="black")

        self.frameCommandGrid.pack()
        
        #Row 1
        self.clear = tk.Button(self.frameCommandGrid, text="Clear", command = lambda: self.btn_clear(), fg="black", width=25, height = 6, bd=0, bg="#FAEBD7", cursor="hand2").grid(row=0,column=0,columnspan=2,padx=1,pady=1)
        self.back = tk.Button(self.frameCommandGrid, text="<", command = lambda: self.btn_back(), fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=0,column=2,padx=1,pady=1)
        self.divide = tk.Button(self.frameCommandGrid, text="/", command = lambda: self.btn_click("/"), fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=0,column=3,padx=1,pady=1)
        #Row2
        
        self.button_7 = tk.Button(self.frameCommandGrid, text="7",  command = lambda: self.btn_click("7"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=0,padx=1,pady=1)
        self.button_8 = tk.Button(self.frameCommandGrid, text="8",  command = lambda: self.btn_click("8"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=1,padx=1,pady=1)
        self.button_9 = tk.Button(self.frameCommandGrid, text="9",  command = lambda: self.btn_click("9"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=1,column=2,padx=1,pady=1)
        self.button_multiply = tk.Button(self.frameCommandGrid, text="*",  command = lambda: self.btn_click("*"),  fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=1,column=3,padx=1,pady=1)
        #Row3

        self.button_4 = tk.Button(self.frameCommandGrid, text="4", command = lambda: self.btn_click("4"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=0,padx=1,pady=1)
        self.button_5 = tk.Button(self.frameCommandGrid, text="5", command = lambda: self.btn_click("5"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=1,padx=1,pady=1)
        self.button_6 = tk.Button(self.frameCommandGrid, text="6", command = lambda: self.btn_click("6"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=2,column=2,padx=1,pady=1)
        self.button_minus = tk.Button(self.frameCommandGrid, text="-", command = lambda: self.btn_click("-"), fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=2,column=3,padx=1,pady=1)
        
        #Row4
        self.button_1 = tk.Button(self.frameCommandGrid, text="1", command = lambda: self.btn_click("1"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=0,padx=1,pady=1)
        self.button_2 = tk.Button(self.frameCommandGrid, text="2", command = lambda: self.btn_click("2"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=1,padx=1,pady=1)
        self.button_3 = tk.Button(self.frameCommandGrid, text="3", command = lambda: self.btn_click("3"), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=3,column=2,padx=1,pady=1)
        self.button_add = tk.Button(self.frameCommandGrid, text="+", command = lambda: self.btn_click("+"), fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=3,column=3,padx=1,pady=1)
        #Row5
        self.button_0 = tk.Button(self.frameCommandGrid, text="0", command = lambda: self.btn_click("0"), fg="black", width=25, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        self.button_dec = tk.Button(self.frameCommandGrid, text=".", command = lambda: self.btn_click("."), fg="black", width=12, height = 6, bd=0, bg="#eee", cursor="hand2").grid(row=4,column=2,padx=1,pady=1)
        self.button_equals = tk.Button(self.frameCommandGrid, text="=", command = lambda: self.btn_equal(), fg="black", width=12, height = 6, bd=0, bg="#97FFFF", cursor="hand2").grid(row=4,column=3,padx=1,pady=1)

        

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()




