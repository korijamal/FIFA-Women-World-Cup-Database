import tkinter as tk

def on_button_click():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")

# Create the main window
root = tk.Tk()
root.title("Basic GUI")
root.geometry("300x200")  # Set the window size

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Click Me", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
