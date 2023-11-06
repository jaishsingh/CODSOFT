import tkinter
import tkinter.messagebox
import pickle

# Create a tkinter window
win = tkinter.Tk()
win.title("To-Do List")

# Function to add a task to the to-do list
def task_adder():
    todo = task_entry.get()
    if todo !="":
        todo_box.insert(tkinter.END, todo)
        task_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="First, enter the task!")

# Function to remove a selected task from the to-do list
def task_remove():
    try:
        selected_index = todo_box.curselection()[0]
        todo_box.delete(selected_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="First, select a task to delete.")

def edit_task():
    try:
        selected_index = todo_box.curselection()[0]
        edited_task = task_entry.get()
        if edited_task != "":
            todo_box.delete(selected_index)
            todo_box.insert(selected_index, edited_task)
            task_entry.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Warning", "Please enter a new task to edit.")
    except:
        tkinter.messagebox.showwarning("Warning", "Please select a task to edit.")


def task_load():
    try:
        with open("tasks.dat", "rb") as file:
            task_list = pickle.load(file)
            todo_box.delete(0, tkinter.END)
            for task in task_list:
                todo_box.insert(tkinter.END, task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning("Warning", "Task file not found.")

def task_save():
    task_list = todo_box.get(0, tkinter.END)
    with open("tasks.dat", "wb") as file:
        pickle.dump(task_list, file)


# Create a frame to hold the to-do list
list_frame = tkinter.Frame(win)
list_frame.pack()

# Create a Listbox to display the tasks
todo_box = tkinter.Listbox(list_frame, height=35, width=75,background=("light blue"))
todo_box.pack(side=tkinter.LEFT)

# Add a scrollbar to the list
scrollbar = tkinter.Scrollbar(list_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
todo_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todo_box.yview)


# Entry widget for entering new tasks
task_entry = tkinter.Entry(win, width=75,background=("light yellow"))
task_entry.pack()

# Buttons for adding, removing, loading, and saving tasks
add_task_button = tkinter.Button(win, text="Add Task", font=("Arial", 10), width=10, command=task_adder,background=("pink"))
add_task_button.pack()

remove_task_button = tkinter.Button(win, text="Remove Task", font=("Arial", 10), width=10, command=task_remove,background=("red"))
remove_task_button.pack()

load_task_button = tkinter.Button(win, text="Load", font=("Arial", 10), width=10, command=task_load,background=("green"))
load_task_button.pack()

save_task_button = tkinter.Button(win, text="Save",font=("Arial", 10), width=10, command=task_save,background=("light green"))
save_task_button.pack()

edit_task_button=tkinter.Button(win,text="Edit",font=("Arial", 10), width=10, command=edit_task,background=("yellow"))
edit_task_button.pack()

# Start the tkinter main loop
win.mainloop()