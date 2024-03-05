import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List App")
root.configure(background='#FFFFFF')  # Set background color

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task, bg='#4CAF50', fg='white')  # Green button
add_button.grid(row=0, column=1, padx=5, pady=10)

listbox = tk.Listbox(root, width=50, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task, bg='#FF5733', fg='white')  # Red button
delete_button.grid(row=2, column=0, padx=5, pady=10)

exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy, bg='#3B5998', fg='white')  # Blue button
exit_button.grid(row=2, column=1, padx=5, pady=10)

root.mainloop()
