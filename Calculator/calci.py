from tkinter import *
import math

expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set("")

def evaluate():
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=""


m=Tk()
m.title('Calculator')
m.config(background='Dark gray')

equation = StringVar()
e=Entry(m,font=('arial',20),insertwidth=3,justify='right',state=DISABLED,bd=4,textvariable=equation)
e.grid(columnspan=4)
b1=Button(m,text='1',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(1))
b1.grid(row=2,column=0)
b2=Button(m,text='2',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(2))
b2.grid(row=2,column=1)
b3=Button(m,text='3',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(3))
b3.grid(row=2,column=2)
b4=Button(m,text='4',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(4))
b4.grid(row=3,column=0)
b5=Button(m,text='5',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(5))
b5.grid(row=3,column=1)
b6=Button(m,text='6',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(6))
b6.grid(row=3,column=2)
b7=Button(m,text='7',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(7))
b7.grid(row=4,column=0)
b8=Button(m,text='8',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(8))
b8.grid(row=4,column=1)
b9=Button(m,text='9',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(9))
b9.grid(row=4,column=2)
b0=Button(m,text='0',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press(0))
b0.grid(row=5,column=1)
b11=Button(m,text='/',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press('/'))
b11.grid(row=2,column=3)
b12=Button(m,text='*',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press('*'))
b12.grid(row=3,column=3)
b13=Button(m,text='+',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press('+'))
b13.grid(row=4,column=3)
b14=Button(m,text='-',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press('-'))
b14.grid(row=5,column=3)
b15=Button(m,text='.',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=lambda:press('.'))
b15.grid(row=5,column=0)
b16=Button(m,text='=',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=evaluate)
b16.grid(row=5,column=2)
b17=Button(m,text='CE',font=('arial',20),activebackground='Blue',padx=16,pady=16,bg='white',bd=4,command=clear)
b17.grid(columnspan=4)
m.mainloop()
