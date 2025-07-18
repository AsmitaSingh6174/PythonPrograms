import tkinter as tk                              #tkinter is python in-built GUI module 
from tkinter import messagebox       #Msgbox is a window pop up jo info ya alert dikhata hai

# App colors and fonts
BG_COLOR = "#f0f4f7"
ENTRY_BG = "#ffffff"
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT = "#ffffff"
FONT = ("Segoe UI", 12)

 # Main app window
app = tk.Tk()
app.title("🌟 To-Do List")
app.geometry("400x500")
app.configure(bg=BG_COLOR)
app.resizable(False, False)

# Label
tk.Label(app, text="📝 Your To-Do List", font=("Segoe UI", 18, "bold"), bg=BG_COLOR, fg="#333").pack(pady=20)

# Entry for typing tasks
task_entry = tk.Entry(app, font=FONT, bg=ENTRY_BG, width=28, bd=2)
task_entry.pack(pady=10)

# Frame to hold buttons
btn_frame = tk.Frame(app, bg=BG_COLOR)
btn_frame.pack(pady=5)

# Add Task Function
def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Empty Field", "Please enter a task!")
    else:
        task_listbox.insert(tk.END, f"🔹 {task}")
        task_entry.delete(0, tk.END)

# Delete Task Function
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showinfo("No Selection", "Please select a task to delete.")

# Buttons
add_btn = tk.Button(btn_frame, text="➕ Add Task", font=FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT, padx=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="❌ Delete Task", font=FONT, bg="crimson", fg=BUTTON_TEXT, padx=10, command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

# Listbox for tasks
task_listbox = tk.Listbox(app, font=("Segoe UI", 12), width=35, height=15, bd=2, selectbackground="#d1e7dd", activestyle="none")
task_listbox.pack(pady=20)

# Run the app
app.mainloop()
