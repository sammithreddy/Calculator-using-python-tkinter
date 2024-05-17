from tkinter import *
class calci():
    def __init__(self):
        self.root=Tk()

        self.ans=""
        self.numbers=["0","1","2","3","4","5","6","7","8","9"]

        #Setting the geometry
        self.root.geometry("800x400")
        #Setting the font in a tuple
        self.Font=("Arial",20)
        #Creating a button frame
        #self.textbox=Text(self.root,height=2,width=20)
        #self.textbox.pack(padx=20,pady=10)
        self.e=Entry(self.root,width=35,borderwidth=5)
        self.e.pack()

        self.buttonframe=Frame(self.root)
        self.buttonframe.columnconfigure(0,weight=1)
        self.buttonframe.columnconfigure(1,weight=1)
        self.buttonframe.columnconfigure(2,weight=1)

        self.zero=Button(self.buttonframe,text="0",font=self.Font,command=lambda: self.getsymbol("0"))
        self.zero.grid(row=0,column=0,sticky="NEWS")

        self.one=Button(self.buttonframe,text="1",font=self.Font,command=lambda: self.getsymbol("1"))
        self.one.grid(row=0,column=1,sticky="NEWS")

        self.two=Button(self.buttonframe,text="2",font=self.Font,command=lambda: self.getsymbol("2"))
        self.two.grid(row=0,column=2,sticky="NEWS")

        self.three=Button(self.buttonframe,text="3",font=self.Font,command=lambda: self.getsymbol("3"))
        self.three.grid(row=1,column=0,sticky="NEWS")

        self.four=Button(self.buttonframe,text="4",font=self.Font,command=lambda: self.getsymbol("4"))
        self.four.grid(row=1,column=1,sticky="NEWS")

        self.five=Button(self.buttonframe,text="5",font=self.Font,command=lambda: self.getsymbol("5"))
        self.five.grid(row=1,column=2,sticky="NEWS")

        self.six=Button(self.buttonframe,text="6",font=self.Font,command=lambda: self.getsymbol("6"))
        self.six.grid(row=2,column=0,sticky="NEWS")

        self.seven=Button(self.buttonframe,text="7",font=self.Font,command=lambda: self.getsymbol("7"))
        self.seven.grid(row=2,column=1,sticky="NEWS")

        self.eight=Button(self.buttonframe,text="8",font=self.Font,command=lambda: self.getsymbol("8"))
        self.eight.grid(row=2,column=2,sticky="NEWS")

        self.nine=Button(self.buttonframe,text="9",font=self.Font,command=lambda: self.getsymbol("9"))
        self.nine.grid(row=3,column=0,sticky="NEWS")

        self.plus=Button(self.buttonframe,text="+",font=self.Font,command=lambda: self.getsymbol("+"))
        self.plus.grid(row=3,column=1,sticky="NEWS")

        self.minus=Button(self.buttonframe,text="-",font=self.Font,command=lambda: self.getsymbol("-"))
        self.minus.grid(row=3,column=2,sticky="NEWS")

        self.divide=Button(self.buttonframe,text="/",font=self.Font,command=lambda: self.getsymbol("/"))
        self.divide.grid(row=4,column=0,sticky="NEWS")

        self.multiply=Button(self.buttonframe,text="*",font=self.Font,command=lambda: self.getsymbol("*"))
        self.multiply.grid(row=4,column=1,sticky="NEWS")

        self.equal=Button(self.buttonframe,text="=",font=self.Font,command=lambda: self.getsymbol("="))
        self.equal.grid(row=4,column=2,sticky="NEWS")

        self.back=Button(self.buttonframe,text="Clear",font=self.Font,command=lambda: self.getsymbol("x"))
        self.back.grid(row=5,column=0,sticky="NEWS")

        self.buttonframe.pack(fill='x')
        self.root.mainloop()
    def getsymbol(self,var):
        if var=="x":
            self.e.delete("end","end")
        if var in self.numbers:
            self.ans=self.ans+var
            self.e.insert("end",var)
        elif var!="=":
            self.ans=self.ans+var
            self.e.delete(0,"end")
        else:
            self.e.delete(0,"end")
            self.e.insert(0,eval(self.ans))
            self.ans=str(eval(self.ans))
calci()