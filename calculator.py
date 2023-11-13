import tkinter as tk
from tkinter import*

def click(event):
    global cal
    text=event.widget.cget("text")
    print(text)

    if text=="=":
        if cal.get().isdigit():
            value=int(cal.get())
        else:
            try:
                value=eval(cal.get())
            except Exception as e:
                value="SYNTAX ERROR"

        cal.set(value)
        cal.update()


    elif text=="C":
        cal.set("")
        cal.update()
    else:
        cal.set(cal.get() + text)
        cal.update()


root=Tk()

root.geometry("400x550")
root.title("Simple Calculator")


cal=StringVar()
cal.set("")
display=Entry(root,textvar=cal,font="Calibri 30",background="yellow")
display.pack(fill=X,  ipadx=6 ,ipady=6)

frame1=Frame(root,background="gray")
button=Button(frame1,text="9",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text="8",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="7",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,background="gray")
button=Button(frame1,text="6",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text="5",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="4",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,background="gray")
button=Button(frame1,text="3",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text="2",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="1",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,background="gray")
button=Button(frame1,text="0",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=11,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text=".",font="Calibri 18",padx=24,pady=20,background="light gray")
button.pack(side=RIGHT,padx=12,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="C",font="Calibri 18",padx=20,pady=20,background="light gray")
button.pack(side=RIGHT,padx=9,pady=9)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,background="gray")
button=Button(frame1,text="/",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text="*",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="+",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)
frame1.pack()
frame1=Frame(root,background="gray")
button=Button(frame1,text="-",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)


button=Button(frame1,text="%",font="Calibri 18",padx=21,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)

button=Button(frame1,text="=",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT,padx=10,pady=9)
button.bind("<Button-1>",click)
frame1.pack()



root.mainloop()