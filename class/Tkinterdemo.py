# crud operation 
from tkinter import *
import mysql.connector as mc
import tkinter.messagebox as tm


def query_conn():
    return mc.connect(
        host="localhost",
        user="root",
        password="",
        database="myserver")
    
# query_conn()
                                            
def c_clear():  
              
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_email.delete(0, "end")
        e_mobile.delete(0, "end")
        
def c_submit():  
    print("clicked on submit button")
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" :
        tm.showinfo("insert status", "All given details are mandatory.")
    else:
        conn=query_conn()
        cursor=conn.cursor()
        query="insert into emp (FirstName, LastName, EmailID, MobileNo) values(%s,%s,%s,%s)"
        arg=(e_fname.get(), e_lname.get(), e_email.get(), e_mobile.get())
        cursor.execute(query, arg)
        conn.commit()
        conn.close()
        tm.showinfo("insert status", "Data stored successfully.")
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_email.delete(0, "end")
        e_mobile.delete(0, "end")

    
def c_search():
    c_clear()
    if e_id.get()=="":
        tm.showinfo("Search status", "ID is mandatory for search")
    
    else:
        conn=query_conn()
        cursor=conn.cursor()
        query="select * from emp where ID=%s"
        arg=(e_id.get(),)
        cursor.execute(query, arg)
        raw=cursor.fetchall()
        if (raw):
            for i in raw:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
            conn.commit()
            conn.close()
        else:
             tm.showinfo("Search Status", "Data Not found.")

def c_update():

    if e_id.get()=="" and (e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()==""):
        tm.showinfo("Upadate status", "It is mandatory to all field.")

    else:
        conn=query_conn()
        cursor=conn.cursor()
        query="update emp set FirstName=%s,LastName=%s, EmailID=%s, MobileNo=%s,ID=%s where ID=%s"
        arg=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get(),e_id.get())
        cursor.execute(query, arg)
        conn.commit()
        conn.close()
        tm.showinfo("Update status", "Data updated successfully.")
        e_fname.delete(0, "end")


def c_delete():
    if e_id.get()=="":
        tm.showinfo("Delete status", "ID is mandatory for delete")
    else:
        conn=query_conn()
        cursor=conn.cursor()
        query="delete from emp where ID=%s"
        arg=(e_id.get(),)
        cursor.execute(query, arg)
        conn.commit()
        conn.close()    
        tm.showinfo("Delete status", "Data deleted successfully.")
        e_fname.delete(0, "end")

root=Tk()
root.geometry("400x400")






l_id=Label(root, text="ID: ", font="arial 14")
l_id.place(x=40, y=50)

e_id=Entry()
e_id.place(x=200, y=50)

l_fname=Label(root, text="First Name: ", font="arial 14")
l_fname.place(x=40, y=100)

e_fname=Entry()
e_fname.place(x=200, y=100)

l_lname=Label(root, text="Last Name: ", font="arial 14")
l_lname.place(x=40, y=150)

e_lname=Entry()
e_lname.place(x=200, y=150)

l_email=Label(root, text="Email: ", font="arial 14")
l_email.place(x=40, y=200)

e_email=Entry()
e_email.place(x=200, y=200)

l_mobile=Label(root, text="Mobile No.:: ", font="arial 14")
l_mobile.place(x=40, y=250)

e_mobile=Entry()
e_mobile.place(x=200, y=250)

b_submit=Button(root, text="submit", font="arial 12",bg= "grey27",fg="white", command=c_submit)
b_submit.place(x=40, y=300)

b_search=Button(root, text="Search",bg= "grey27", fg="white", font="arial 12", command=c_search)
b_search.place(x=120, y=300)

b_update=Button(root, text="Upadate",bg= "grey27", fg="white", font="arial 12",command=c_update)
b_update.place(x=200, y=300)

b_delete=Button(root, text="Delete", font="arial 12",bg= "grey27", fg="white",command=c_delete)
b_delete.place(x=290, y=300)

b_clear=Button(root, text="Clear", font="arial 12",bg= "grey27", fg="white",command=c_clear)
b_clear.place(x=160, y=350)


root.mainloop()