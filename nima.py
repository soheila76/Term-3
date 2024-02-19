import tkinter as tk

def save_schedule():
    
    pass
def alaki(event):
    n=var.get()
    print(n)
    if n == 1:
        work="Breakfast"
        entry.insert(0,work)
    elif n == 2:
        work="Lunch"
    elif n == 3:
        work = "Dinner"
    elif n == 4:
        work = "Sleep"
    elif n == 5:
        work= "Go to class"
    
    

root = tk.Tk()
root.title("Daily Schedule Planner")
root.geometry("900x600")


weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i, day in enumerate(weekdays):
    lbl=tk.Label(root, text=day)
    lbl.grid(row=0, column=i)



for i in range(1, 7):  
    for j in range(7): 
        entry = tk.Entry(root)
        entry.grid(row=i, column=j)
        entry.bind("<1>", alaki)


tk.Label(root, text="Daily Tasks:").grid(row=7, column=0)

tasks = {
    "Breakfast": 1,
    "Lunch": 2,
    "Dinner": 3,
    "Sleep": 4,
    "Go to class": 5
}
var = tk.IntVar(root, 1) 
for task, val in tasks.items():
    tk.Radiobutton(root, text=task, variable=var, value=val).grid(row=val+7, column=0)


save_button = tk.Button(root, text="Save", command=save_schedule)
save_button.grid(row=13, column=3, columnspan=3)

root.mainloop()

