from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry("400x400")

expression=""
input_text=StringVar()

input_field = Entry(window, font = ('arial', 18, 'bold'), textvariable =input_text, width = 50, bg = "#A9A9A9", bd = 0, justify = RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=16)

btn_frame=Frame(window,width=312,height=272,bg="#D3D3D3")
btn_frame.pack()


def btn_clicked(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clr():
    global expression
    expression=""
    input_text.set(expression)

def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""

button7=Button(btn_frame,text="7",width="7",height="3",fg="black",command=lambda: btn_clicked(7))
button7.grid(row=2,column=0)
button8=Button(btn_frame,text="8",width="7",height="3",fg="black",command=lambda: btn_clicked(8))
button8.grid(row=2,column=1)
button9=Button(btn_frame,text="9",width="7",height="3",fg="black",command=lambda: btn_clicked(9))
button9.grid(row=2,column=2)
buttondiv=Button(btn_frame,text="/",width="7",height="3",fg="black",command=lambda: btn_clicked("/"))
buttondiv.grid(row=2,column=3)

button4=Button(btn_frame,text="4",width="7",height="3",fg="black",command=lambda: btn_clicked(4))
button4.grid(row=3,column=0)
button5=Button(btn_frame,text="5",width="7",height="3",fg="black",command=lambda: btn_clicked(5))
button5.grid(row=3,column=1)
button6=Button(btn_frame,text="6",width="7",height="3",fg="black",command=lambda: btn_clicked(6))
button6.grid(row=3,column=2)
buttonmul=Button(btn_frame,text="x",width="7",height="3",fg="black",command=lambda: btn_clicked("x"))
buttonmul.grid(row=3,column=3)

button1=Button(btn_frame,text="1",width="7",height="3",fg="black",command=lambda: btn_clicked(1))
button1.grid(row=4,column=0)
button2=Button(btn_frame,text="2",width="7",height="3",fg="black",command=lambda: btn_clicked(2))
button2.grid(row=4,column=1)
button3=Button(btn_frame,text="3",width="7",height="3",fg="black",command=lambda: btn_clicked(3))
button3.grid(row=4,column=2)
buttonminus=Button(btn_frame,text="-",width="7",height="3",fg="black",command=lambda: btn_clicked("-"))
buttonminus.grid(row=4,column=3)

button_point=Button(btn_frame,text=".",width="7",height="3",fg="black",command=lambda: btn_clicked("."))
button_point.grid(row=5,column=0)
button_zero=Button(btn_frame,text="0",width="7",height="3",fg="black",command=lambda: btn_clicked(0))
button_zero.grid(row=5,column=1)
button_plus=Button(btn_frame,text="+",width="7",height="7",fg="black",command=lambda: btn_clicked("+"))
button_plus.grid(row=5,column=2,rowspan=2)
button_clear=Button(btn_frame,text="C",width="7",height="7",fg="black",command=lambda: btn_clr(),bg="#A9A9A9")
button_clear.grid(row=5,column=3,rowspan=2)


button_equal=Button(btn_frame,text="=",width=18,height="3",fg="black",bg="#A9A9A9",command=lambda: btn_equal() )
button_equal.grid(row=6,columnspan=2)





window.mainloop()