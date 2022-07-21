from tkinter import *

root=Tk()
# root.geometry("300x300")





# def add(lab):
#     p=lab.split("+")
#     return p[0]+p[1]
 
    
# if "+"in memory:
#     add(memory)
memory=""
def show(a):
    global memory
    
    memory=memory+a
    lab.config(text=memory)


frame1=Frame(root, bg="red", borderwidth=8,width=300, height= 400)
display=Canvas(frame1, bg="grey", borderwidth=8,width=200, height= 50)
frame1.pack()
display.grid(row=0,columnspan=4, pady =10 )
lab=Label(display, text=memory,bg="black", fg= "white")
lab.grid(column=0, row=0)
# btn1=Button(frame1, text="Naresh",borderwidth=6, )
  
b=0
a=1
for i in range(9,0,-1):
    print(i)
    btn=Button(frame1,text=" "+str(i)+" ", font="arial 24 bold",command=show(str(i)) )
    if i%3==0 :
        a+=1
    btn.grid(row= a, column=b)
    
    if b==2:
        b=0
    else:
        b+=1


a,b=1,0
op=["^","%","/","C","x","-","+"]
for i in op:
    opr= Button(frame1,text=" "+i+" ", font="arial 24 bold",command=show(i)  )
    opr.grid(row= a, column=b)
    if b==3:
        a+=1
    if b<3:
        b+=1
    



# btn1.pack()


root.mainloop()


