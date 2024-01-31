import tkinter as tk

tasks = []  # Initialize the task list

def add_task():
    """Adds a new task to the list."""
    task_description = task_entry.get()
    tasks.append(task_description)
    task_listbox.insert(tk.END, task_description)
    task_entry.delete(0, tk.END)  # Clear the entry field

def view_tasks(filter_type):
    """Displays tasks based on the selected filter."""
    task_listbox.delete(0, tk.END)  # Clear the listbox
    filtered_tasks = []
    if filter_type == "all":
        filtered_tasks = tasks
    elif filter_type == "pending":
        filtered_tasks = [task for task in tasks if task.startswith("-")]

    elif filter_type == "completed":
        filtered_tasks = [task for task in tasks if task.startswith("*")]
    # Add more filters as needed (e.g., completed, prioritized)

    for task in filtered_tasks:
        task_listbox.insert(tk.END, task)

root =tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

view_all_button = tk.Button(root, text="View All", command=lambda: view_tasks("all"))
view_all_button.pack()

view_pending_button = tk.Button(root, text="View Pending", command=lambda: view_tasks("pending"))
view_pending_button.pack()

view_completed_button = tk.Button(root, text="View Completed", command=lambda: view_tasks("completed"))
view_completed_button.pack()
# Add more buttons for other filters as needed

task_listbox = tk.Listbox(root)
task_listbox.pack()

root.mainloop()
