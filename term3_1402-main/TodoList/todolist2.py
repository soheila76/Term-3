from tkinter import *
def handler(event):
    d = jobEntry.get()
    todo[d] = Checkbutton(frame, command=lambda:check(d))
    show_todo()
def show_todo():
    x=0
    for k,v in todo.items():
        print("********",v)
        v.grid(row=x, column=0)
        Label(frame, text = k).grid(row=x, column=1)
        x+=1
    # todo["a"].place(x=0,y=200)

def check(x):
    del todo[x]
    clear_frame()
    print(todo)
    show_todo()
def clear_frame():
    global frame
    frame.place_forget()
    frame = Frame(root)
    frame.place(x=0, y=100)
    # test=Label(frame,text="test")
    # test.pack()
    # root.update()
    
   
    
    

todo = {}
doing = []
done = []
todo_checkbutton =[]
root = Tk()
root.geometry("600x400")
jobLbl = Label(root, text = "Job", font=("", 12))
jobLbl.place(x=0, y=20)
jobEntry = Entry(root)
jobEntry.place(x=40, y=20)
jobEntry.bind('<Return>',handler)
todo_lbl = Label(root, text = "Todo",font=("", 12,"bold"),bg="brown",width=20)
todo_lbl.place(x=0, y=50)
doing_lbl = Label(root, text = "Doing",font=("", 12,"bold"),bg="khaki",width=20)
doing_lbl.place(x=200, y=50)
doing_lbl = Label(root, text = "Done",font=("", 12,"bold"),bg="light green",width=20)
doing_lbl.place(x=400, y=50)
frame = Frame(root)
frame.place(x=0, y=100)
# test=Label(frame,text="test")
# test.pack()
root.mainloop()