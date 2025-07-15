import tkinter as tk

def add_task():                                                             # Function to add a task
    task = task_entry.get().strip()                                 # Remove extra spaces
    if task == "":
        task_label.config(text="❌ Please write something!")
    else:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        task_label.config(text="📝 Task added!")

def delete_task():                                                         # Function to delete a task
    selected = tasks_listbox.curselection()                  # Get selected item index
    if selected:                                                                 # If something is selected
        tasks_listbox.delete(selected[0])                        # Delete that index
        task_label.config(text="🗑 Task deleted!")
    else:
        task_label.config(text="❌ No task selected!")

window = tk.Tk()                                                            # Window setup
window.title("To-Do List App")
window.geometry("300x400")
window.config(bg="lavender")

                                                                                          # Label for status
task_label = tk.Label(window, text="📋 Manage your tasks!", bg="lavender", font=("Arial", 12, "bold"))
task_label.pack(pady=10)

task_entry = tk.Entry(window, font=("Arial", 12))      # Entry for task input
task_entry.pack(pady=5)

                                                                                           # Add task button
add_button = tk.Button(window, text="➕ Add Task", command=add_task, bg="darkgreen", fg="white", font=("Arial", 10, "bold"))
add_button.pack(pady=5)

                                                                                           # Task list display
tasks_listbox = tk.Listbox(window, font=("Arial", 12), height=10, width=30)
tasks_listbox.pack(pady=10)

                                                                                           # Delete task button
delete_button = tk.Button(window, text="❌ Delete Task", command=delete_task, bg="crimson", fg="white", font=("Arial", 10, "bold"))
delete_button.pack(pady=5)

window.mainloop()                                                          # Start the app
