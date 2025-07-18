import tkinter as tk
from tkinter import scrolledtext
import random

# 💬 Predefined responses
responses = {
    "hi": ["Hello! 😊", "Hey there! 👋", "Hi! How can I assist you today?"],
    "hello": ["Hi! 👋", "Nice to see you! 🤗", "Hey! 😄"],
    "how are you": ["Doing great! Thanks! 🧠", "Better now that you're here! 😄"],
    "what is your name": ["I'm Pixie 🤖", "You can call me ChatBuddy 💬"],
    "bye": ["Goodbye! 👋", "Take care! 💖", "See you again! 🫡"],
    "thanks": ["You're welcome! 🤝", "Glad I could help! ✨", "Anytime! 😊"],
    "default": ["Hmm... I'm still learning that 🤔", "Could you say that differently? 🧠", "I didn't get that. 😅"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# 📨 Send message
def send_message():
    user_message = entry_box.get()
    if user_message.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You ‍♀️: {user_message}\n", "user")
    bot_response = get_response(user_message)
    chat_window.insert(tk.END, f"Bot 🤖: {bot_response}\n\n", "bot")
    chat_window.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)
    chat_window.yview(tk.END)

# 🖼 GUI setup
root = tk.Tk()
root.title("ChatBot UI")
root.geometry("500x600")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# 🔲 Frame for the chat window
chat_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.FLAT)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, font=("Segoe UI", 12), bg="#ffffff", fg="#333333")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.DISABLED)

# 🎨 Custom tags for styling
chat_window.tag_config("user", foreground="#1e88e5", font=("Segoe UI", 12, "bold"))
chat_window.tag_config("bot", foreground="#43a047", font=("Segoe UI", 12, "italic"))

# Entry + Send layout
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry_box = tk.Entry(entry_frame, font=("Segoe UI", 12), bg="#ffffff", fg="#000000", relief=tk.FLAT, bd=2)
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
entry_box.bind("<Return>", lambda event=None: send_message())

send_button = tk.Button(entry_frame, text="Send 💬", command=send_message,
                        font=("Segoe UI", 11, "bold"), bg="#1e88e5", fg="white", activebackground="#1565c0",
                        relief=tk.FLAT, padx=15, pady=5, bd=0)
send_button.pack(side=tk.RIGHT)

# Greeting
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Bot 🤖: Hello! I’m Pixie. How can I help you today? 🧠\n\n", "bot")
chat_window.config(state=tk.DISABLED)

# Run
root.mainloop()
