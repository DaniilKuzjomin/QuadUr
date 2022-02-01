from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

#2, 4, -12

D=-1
t="Нет решений"
graf=False

def solution():
    global D,t,graf
    if En1.get() !="" and En2.get() !="" and En3.get() !="" :
        if(float(En1.get())==0 and float(En2.get())==0 and float(En3.get())==0):
            l4.configure(text="В данных полях не может быть нуля!")
            En1.configure(bg="#ff0000")
            En1.configure(bg="#ff0000")
            En1.configure(bg="#ff0000")
            graf=False
        elif float(En1.get())==0 and float(En2.get())!=0 and float(En3.get())!=0:
            l4.configure(text="В данном поле не может быть нуля!")
            En1.configure(bg="#ff0000")
            graf=False
        else:
            a=float(En1.get())
            b=float(En2.get())
            c=float(En3.get())
            D=b*b-4*a*c
            if D>0:
                l3_=round((-1*b+sqrt(D))/(2*a),2)
                l1_=round((-1*b-sqrt(D))/(2*a),2)
                t=(f"L1={l1_}, \nL2={l3_}")
                graf=True
            elif D==0:
                l1_=round((-1*b_)/(2*a_),2)
                t=(f"X1={l1}")
                graf=True
            else:
                t=(" ")
                graf=False
    else:
        if En1.get()=="":
            En1.configure(bg="#ff0000")
        if En2.get()=="":
            En2.configure(bg="#ff0000")
        if En3.get()=="":
            En3.configure(bg="#ff0000")
        else:
            En1.configure(bg="lightblue")
            En2.configure(bg="lightblue")
            En3.configure(bg="lightblue")
    return graf,D,t


def bird():
    x1 = np.arange(0, 9.5)
    y1 =(-4/27)*x1**2+6
    x2 = np.arange(-2, 7.5)
    y2 = (1/9)*(x2-7)**2-4
    x3 = np.arange(-4, 0.5)
    y3 = (-0.5)*(x3+2)**2+8
    x4 = np.arange(-6, -1.5)
    y4 = (-1/16)*(x4+2)**2+5
    x5 = np.arange(-6, -3.5)
    y5 = x5+10
    x6 = np.arange(7, 9.5)
    y6 = (-x6)+3
    x7 = np.arange(-6, 1.5)
    y7 = 0.5*x7-1
    x8 = np.arange(-5,2.5)
    y8 = 0.5*x8-2.5
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
    plt.title('Птица')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def glasses():
    x1= np.arange(-9, -0.5, 0.5)
    y1=-(1/16)*(x1+5)**2+2
    x2= np.arange(1,9.5, 0.5)
    y2=-(1/16)*(x2-5)**2+2
    x3= np.arange(-9,-0.5,0.5)
    y3=(1/4)*(x3+5)**2-3
    x4= np.arange(1,9.5,0.5)
    y4=(1/4)*(x4-5)**2-3
    x5= np.arange(-9,-5.5,0.5)
    y5=-(x5+7)**2+5
    x6= np.arange(6,9.5, 0.5)
    y6=-(x6-7)**2+5
    x7= np.arange(-1,1.5,0.5)
    y7=-(0.5)*x7**2+1.5
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def umbr():
    x1 = np.arange(-12, 12.5, 0.5)
    y1 = (-1/18)*x1**2+12
    x2 = np.arange(-4, 4.5, 0.5)
    y2 = (-1/8)*x2**2+6
    x3 = np.arange(-12, -3.5, 0.5)
    y3 = (-1/8)*(x3+8)**2+6
    x4 = np.arange(4, 12.5, 0.5)
    y4 = (-1/8)*(x4-8)**2+6
    x5 = np.arange (-4, 0.2, 0.5)
    y5 = 2*(x5+3)**2-9
    x6 = np.arange(-4, 0.7, 0.5)
    y6 = 1.5*(x6+3)**2-10
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def figure():
    choice=var.get()
    if choice==1:
        bird()
    if choice==2:
        glasses()
    else:
        umbr()



def grafik():
    graf,D,t=solution()
    if graf==True:
        a=float(En1.get())
        b=float(En2.get())
        c=float(En3.get())
        x0=(-b)/(2*a)
        y0=a*x0*x0+b*x0+c
        x1 = np.arange(x0-10, x0+10, 0.5)
        y1=a*x1*x1+b*x1+c
        fig = plt.figure()
        plt.plot(x0, y0, x1, y1,'r-d') # Позволяет вводить много значений "r-d"- точки будут отоброжаться робмиками
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=(f"Вершина параболлы ({x0},{y0})")
    else:
        text=(f"Нет возможности построить график.")
t=0

def plus():
    global t   
    if t==0:
      window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()+200))
      bt_plus.config(text="Уменьшить окно")
      t=1
    else:
      window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()-200))
      bt_plus.config(text="Увеличить окно")
      t=0



window=Tk()
window.title("Квадратные уравнения")
window.geometry("650x210")

fr1=Frame(window,width=650, height=210)
fr1.pack(side=TOP)
fr2=Frame(window,width=650, height=200)
fr2.pack(side=BOTTOM)


l1=Label(fr1, text="Решение квадратного уравнения", height=2,width=28, font="Arial 20", fg="green", bg="lightblue", relief="solid")
l1.pack()

En1=Entry(fr1,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En1.pack(side = LEFT, padx=0, pady=2)

l2=Label(fr1, text="x**2+", height=2,width=4, font="Arial 20", fg="green")
l2.pack(side=LEFT, padx=4,pady=2)

En2=Entry(fr1,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En2.pack(side = LEFT, padx=4, pady=2)

l3=Label(fr1, text="x+", height=2,width=2, font="Arial 20", fg="green")
l3.pack(side=LEFT, padx=4,pady=2)

En3=Entry(fr1,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En3.pack(side = LEFT, padx=3, pady=2)

l31=Label(fr1, text="=0", height=2,width=2, font="Arial 20", fg="green")
l31.pack(side=LEFT, padx=4,pady=2)

resh=Button(fr1,text="Решить",height=2,width=7, font="Arial 15",bg="green",fg="#000000",relief=RAISED, command=solution)
resh.pack(side=LEFT, padx=5,pady=2)

reshgr=Button(fr1,text="График",height=2,width=7, font="Arial 15",bg="green",fg="#000000",relief=RAISED, command=grafik)
reshgr.pack(side=LEFT, padx=5,pady=2)

l4=Label(fr1,text="Решение", height=4,width=60,font="Arial 10",bg="yellow",fg="#000000")
l4.pack(side=BOTTOM,padx=3, pady=0)

bt_plus=Button(fr2,text="Увеличить окно", font="Calibri 26" ,bg="green",command=plus)
bt_plus.pack(side = TOP)
var=IntVar()
r1=Radiobutton(fr2,text="Птичка",variable=var,value=1, font="Calibri 26", command=figure)
r2=Radiobutton(fr2,text="Очки",variable=var,value=2, font="Calibri 26", command=figure)
r3=Radiobutton(fr2,text="Зонтик",variable=var,value=3, font="Calibri 26",command=figure)
r1.pack()
r2.pack()
r3.pack()
bt_plus.bind("<Button-1>",solution)

window.mainloop()
