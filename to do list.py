import tkinter as tk
from tkinter import messagebox
import mysql.connector
#This is done By Mohan Babu Uttaramalluru
db =mysql.connector.connect(host="localhost",user="root",passwd="root",database="todo",charset="utf8")
mycursor=db.cursor()
def add_task():
    task = task_entry.get()
    Priority=priority_entry.get()
    duedate=duedate_entry.get()
    if task:
        cursor = db.cursor()
        cursor.execute("INSERT INTO task (tasks,Priority,duedate) VALUES (%s,%s,%s)", (task,Priority,duedate))
        db.commit()
        cursor.close()
        update_list()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        duedate_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        cursor = db.cursor()
        cursor.execute("DELETE FROM task WHERE tasks = %s", (selected_task,))
        db.commit()
        cursor.close()
def mark_task():
    task = task_entry.get()
    Priority=priority_entry.get()
    duedate=duedate_entry.get()
    M='completed'
    cursor=db.cursor()
    cursor.execute("update task set Remark='completed' WHERE tasks=%s and Priority=%s and duedate=%s",(task,Priority,duedate))
def update_list():
    cursor = db.cursor()
    cursor.execute("SELECT tasks FROM task")
    task = cursor.fetchall()
    cursor.close()
    task_listbox.delete(0, tk.END)
    for tasks in task:
        task_listbox.insert(tk.END, tasks[0])

root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
priority_entry=tk.Entry(root, width=40)
duedate_entry=tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
mark_button=tk.Button(root,text="Remarks",command=mark_task)
task_entry.pack(pady=10)
priority_entry.pack(pady=10)
duedate_entry.pack(pady=10)
add_button.pack()
delete_button.pack()
mark_button.pack()



task_listbox = tk.Listbox(root, width=40)
task_listbox.pack()
root.mainloop()