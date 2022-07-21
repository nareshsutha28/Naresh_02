from tkinter import *

root=Tk()
memory=""
root.geometry("275x410")
root.resizable(0,0)

def clear():
    global memory
    memory="0"
    display.delete(1.0, "end")
    display.insert(1.0, memory)
    
def result():
    global memory
    try:
        memory= str(eval(memory))
        display.delete(1.0, "end")
        display.insert(1.0, memory)
    except:
        display.delete(1.0, "end")
        display.insert(1.0, "Error")
     
    
def show(a):
    global memory
    if memory=="0":
        memory=a
        display.delete(1.0, "end")
        display.insert(1.0, memory)
    else:
        memory+=a
        display.delete(1.0, "end")
        display.insert(1.0, memory)


display=Text(root, bg="grey5",fg="white" ,width=15, height= 2, font="arial 24 bold")

display.grid(row=0,columnspan=4, )
  
Button(root,text=" 1 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("1")).grid(row= 4, column=0)
Button(root,text=" 2 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("2")).grid(row= 4, column=1)
Button(root,text=" 3 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("3")).grid(row= 4, column=2)
Button(root,text=" 4 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("4")).grid(row= 3, column=0)
Button(root,text=" 5 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("5")).grid(row= 3, column=1)
Button(root,text=" 6 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("6")).grid(row= 3, column=2)
Button(root,text=" 7 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("7")).grid(row= 2, column=0)
Button(root,text=" 8 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show('8')).grid(row= 2, column=1)
Button(root,text=" 9 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("9")).grid(row= 2, column=2)
Button(root,text=" ^ ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("**")).grid(row= 1, column=0)
Button(root,text=" % ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show('%')).grid(row= 1, column=1)
Button(root,text=" / ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("/")).grid(row= 1, column=2)
Button(root,text=" C ",bg="red",fg="white" , font="arial 24 bold",width= 3,command=clear).grid(row= 1, column=3)
Button(root,text=" x ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("*")).grid(row= 2, column=3)
Button(root,text=" - ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("-")).grid(row= 3, column=3)
Button(root,text=" + ",bg="grey5",fg="white" , font="arial 24 bold",height=2,pady=15,width= 3,command=lambda:show("+")).grid(row= 4,rowspan=2, column=3)
Button(root,text=" = ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=result).grid(row= 5, column=2)
Button(root,text=" 0 ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show("0")).grid(row= 5, column=0)
Button(root,text=" . ",bg="grey5",fg="white" , font="arial 24 bold",width= 3,command=lambda:show(".")).grid(row= 5, column=1)


root.mainloop()


