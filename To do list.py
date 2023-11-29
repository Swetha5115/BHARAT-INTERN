import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

window = tk.Tk()
window.title("To-Do List App")

task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

window.mainloop()