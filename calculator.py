from tkinter import*
root=Tk()


root.title("CALCULATOR")
textin=StringVar()
operator=""
def clickbutn(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)
def equalbutn():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=""


def equalbutn():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ""


def equalbutn():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ""


def equalbutn():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ""
def clrbutn():
    textin.set(' ')

E=Entry(root,textvar=textin,width=35,bd=30,insertwidth=4,bg="powder blue").grid(columnspan=4)

butn7=Button(root,text="7",padx=40,pady=20,command=lambda:clickbutn("7")).grid(row=1,column=0)
butn8=Button(root,text="8",padx=40,pady=20,command=lambda:clickbutn("8")).grid(row=1,column=1)
butn9=Button(root,text="9",padx=40,pady=20,command=lambda:clickbutn("9")).grid(row=1,column=2)
butn4=Button(root,text="4",padx=40,pady=20,command=lambda:clickbutn("4")).grid(row=2,column=0)
butn5=Button(root,text="5",padx=40,pady=20,command=lambda:clickbutn("5")).grid(row=2,column=1)
butn6=Button(root,text="6",padx=40,pady=20,command=lambda:clickbutn("6")).grid(row=2,column=2)
butn1=Button(root,text="1",padx=40,pady=20,command=lambda:clickbutn("1")).grid(row=3,column=0)
butn2=Button(root,text="2",padx=40,pady=20,command=lambda:clickbutn("2")).grid(row=3,column=1)
butn3=Button(root,text="3",padx=40,pady=20,command=lambda:clickbutn("3")).grid(row=3,column=2)
butn0=Button(root,text="0",padx=40,pady=20,command=lambda:clickbutn("0")).grid(row=4,column=0)

butnC=Button(root,text="C",padx=40,pady=20,command=lambda:clrbutn()).grid(row=4,column=1)
butnEQ=Button(root,text="=",padx=40,pady=20,command=lambda:equalbutn()).grid(row=4,column=2)
butnadd=Button(root,text="+",padx=40,pady=20,command=lambda:clickbutn("+")).grid(row=1,column=3)
butnmul=Button(root,text="*",padx=40,pady=20,command=lambda:clickbutn("*")).grid(row=2,column=3)
butndiv=Button(root,text="/",padx=40,pady=20,command=lambda:clickbutn("/")).grid(row=3,column=3)
butndif=Button(root,text="-",padx=40,pady=20,command=lambda:clickbutn("-")).grid(row=4,column=3)

root.mainloop()

