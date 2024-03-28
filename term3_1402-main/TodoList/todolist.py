from tkinter import *
def handler(event):
    add_todo_task()
def add_todo_task():
    d = jobEntry.get()
    todo.append(d)
    todo_list_update()    
    jobEntry.delete(0, 'end')
def clear_todo_list():  
    todo_listbox.delete(0, 'end') 
def todo_list_update():  
    clear_todo_list()  
    for task in todo:  
        todo_listbox.insert('end', task)
def delete_todo_task():      
    the_value = todo_listbox.get(todo_listbox.curselection())    
    if the_value in todo:   
        todo.remove(the_value)    
        todo_list_update()
# doing
def add_doing_task(item):
    doing.append(item)
    doing_list_update()    
def clear_doing_list():  
    doing_listbox.delete(0, 'end') 
def doing_list_update():  
    clear_doing_list()  
    for task in doing:  
        doing_listbox.insert('end', task)
def delete_doing_task(the_value):      
    if the_value in doing:   
        doing.remove(the_value)    
        doing_list_update()
def move_doing():
    the_value = todo_listbox.get(todo_listbox.curselection())    
    add_doing_task(the_value)
    delete_todo_task()
# done
def add_done_task(item):
    done.append(item)
    done_list_update()    
def clear_done_list():  
    done_listbox.delete(0, 'end') 
def done_list_update():  
    clear_done_list()  
    for task in done:  
        done_listbox.insert('end', task)
def delete_done_task(the_value):      
    if the_value in done:   
        done.remove(the_value)    
        done_list_update()
def move_done():
    the_value = doing_listbox.get(doing_listbox.curselection())    
    add_done_task(the_value)
    delete_doing_task(the_value)

def delete_done_task():      
    the_value = done_listbox.get(done_listbox.curselection())    
    if the_value in done:   
        done.remove(the_value)    
        done_list_update()


        
todo = []
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
# todo frame
todo_frame = Frame(root)
todo_frame.place(x=0, y=100)
todo_listbox = Listbox(  
    todo_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)
todo_listbox.grid(row=0, column=0, padx= 20)
del_todo_btn = Button(root, text="   del   ", command=delete_todo_task)
del_todo_btn.place(x=40, y=320)
doing_btn = Button(root, text="doing", command=move_doing)
doing_btn.place(x=100, y=320)

# doing frame
doing_frame = Frame(root)
doing_frame.place(x=200, y=100)
doing_listbox = Listbox(  
    doing_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)
doing_listbox.grid(row=0, column=0, padx= 20)
done_btn = Button(root, text="done", command=move_done)
done_btn.place(x=280, y=320)

# done frame
done_frame = Frame(root)
done_frame.place(x=400, y=100)
done_listbox = Listbox(  
    done_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)
done_listbox.grid(row=0, column=0, padx= 20)
del_done_btn = Button(root, text="   del   ", command=delete_done_task)
del_done_btn.place(x=480, y=320)
root.mainloop()