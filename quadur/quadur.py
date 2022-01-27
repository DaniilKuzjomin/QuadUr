from tkinter import *


#a = En1.get()
#b = En2.get()
#c = En3.get()

def solution(event):   
    if En1.get() !="" and En2.get() !="" and En3.get() !="" :
        En1.configure(bg="lightblue")
        En2.configure(bg="lightblue")
        En3.configure(bg="lightblue")
    else:
        if En1.get()=="":
            En1.configure(bg="#ff0000")
        if En2.get()=="":
            En2.configure(bg="#ff0000")
        if En3.get()=="":
            En3.configure(bg="#ff0000")






window=Tk()
window.title("Квадратные уравнения")
window.geometry("650x300")


l1=Label(window, text="Решение квадратного уравнения", height=2,width=28, font="Arial 20", fg="green", bg="lightblue", relief="solid")
l1.pack()

En1=Entry(window,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En1.pack(side = LEFT, padx=0, pady=2)

l2=Label(window, text="x**2+", height=2,width=4, font="Arial 20", fg="green")
l2.pack(side=LEFT, padx=4,pady=2)

En2=Entry(window,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En2.pack(side = LEFT, padx=4, pady=2)

l3=Label(window, text="x+", height=2,width=2, font="Arial 20", fg="green")
l3.pack(side=LEFT, padx=4,pady=2)

En3=Entry(window,width=3,font="Arial 20", fg="green", bg="lightblue",justify=LEFT)
En3.pack(side = LEFT, padx=3, pady=2)

l3=Label(window, text="=0", height=2,width=2, font="Arial 20", fg="green")
l3.pack(side=LEFT, padx=4,pady=2)

resh=Button(window,text="Решить",height=2,width=7, font="Arial 15",bg="green",fg="#000000",relief=RAISED)
resh.pack(side=LEFT, padx=5,pady=2)
resh.bind("<Button-1>", solution)

l4=Label(window,text="Решение", height=4,width=60,font="Arial 10",bg="yellow",fg="#000000")
l4.pack(side=BOTTOM,padx=3, pady=0)


window.mainloop()
