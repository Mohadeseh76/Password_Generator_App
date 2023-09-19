import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        

        # Create the password text widget and Copy Password button side by side
        self.password_frame = tk.Frame(root, bg="darkgoldenrod1" ,padx=70, pady=20, relief="flat", borderwidth=10)
        self.password_frame.pack()

        self.instruction_label = tk.Label(self.password_frame, text="Do You Want to Generate a Strong Password?", font=("Comic Sans MS", 20, "bold"), fg="cyan4" ,bg="darkgoldenrod1" )
        self.instruction_label.grid(row=0, column=0, columnspan=10, padx=10, pady=0, sticky="w")

        self.password_text = tk.Entry(self.password_frame, width=40 , bg="aliceblue",font=("Helvetica", 20, "bold") )
        self.password_text.grid(row=1, column=0, padx=5 , pady=20)

        self.copy_button = tk.Button(self.password_frame, text="Copy Password", command=self.copy_to_clipboard , font=("Comic Sans MS", 11, "bold"), fg="darkgoldenrod1", bg="cyan4", relief="ridge", borderwidth=5)
        self.copy_button.grid(row=1, column=1, padx=5)

        # Create and place the Generate Password button
        self.generate_button = tk.Button(self.password_frame, text="GENERATE RANDOM PASSWORD!", command=self.generate_password, font=("Comic Sans MS", 18, "bold"), fg="darkgoldenrod1" , bg="cyan4" , relief="ridge", borderwidth=10)
        self.generate_button.grid(row=3, column=0 , padx=5 , pady=20)

        # Create the settings frame to group widgets
        self.settings_frame = tk.Frame(root,bg="cyan4")
        self.settings_frame.pack()

        self.instruction_label = tk.Label(self.settings_frame, text="Use the settings below to specify the desired length and character parameters when generating your random password.", font=("Comic Sans MS", 11, "bold"), fg="black" ,bg="darkgoldenrod1" )
        self.instruction_label.grid(row=0, column=0, columnspan=100, padx=10, pady=10, sticky="w")

        self.use_uppercase = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(self.settings_frame, text="Allow Uppercase", variable=self.use_uppercase, bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.uppercase_check.grid(row=2, column=0, sticky="w", padx=10)

        self.use_lowercase = tk.BooleanVar()
        self.lowercase_check = tk.Checkbutton(self.settings_frame, text="Allow Lowercase", variable=self.use_lowercase, bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.lowercase_check.grid(row=3, column=0, sticky="w", padx=10)

        self.use_digits = tk.BooleanVar()
        self.digits_check = tk.Checkbutton(self.settings_frame, text="Allow Numbers", variable=self.use_digits, bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.digits_check.grid(row=4, column=0, sticky="w", padx=10)

        self.use_symbols = tk.BooleanVar()
        self.symbols_check = tk.Checkbutton(self.settings_frame, text="Allow Symbols", variable=self.use_symbols, bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.symbols_check.grid(row=5, column=0, sticky="w", padx=10)

        self.exclude_duplicates = tk.BooleanVar()
        self.exclude_duplicates_check = tk.Checkbutton(self.settings_frame, text="Exclude Duplicate Characters", variable=self.exclude_duplicates, bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.exclude_duplicates_check.grid(row=6, column=0, columnspan=2, sticky="w", padx=10)

        self.length_label = tk.Label(self.settings_frame, text="Password Length", bg="cyan4" , font=("Comic Sans MS", 18, "bold"))
        self.length_label.grid(row=1, column=0, sticky="w", padx=40)

        self.length_combobox = ttk.Combobox(self.settings_frame, values=list(range(1, 101)), state="readonly" , width=5, font=("Comic Sans MS", 10, "bold"))
        self.length_combobox.set(8)  # Default length
        self.length_combobox.grid(row=1, column=1, sticky="w", padx=10)

    def generate_password(self):
        char_types = ""
        if self.use_uppercase.get():
            char_types += string.ascii_uppercase
        if self.use_lowercase.get():
            char_types += string.ascii_lowercase
        if self.use_digits.get():
            char_types += string.digits
        if self.use_symbols.get():
            char_types += "!@#$%^&*()_+=<>{}[]~"
        
        if self.exclude_duplicates.get():
            char_types = ''.join(set(char_types))  # Remove duplicates

        length = int(self.length_combobox.get())
        generated_password = ''.join(random.choice(char_types) for _ in range(length))
        self.password_text.delete(0, "end")  # Clear previous text
        self.password_text.insert(0, generated_password)

    def copy_to_clipboard(self):
        generated_password = self.password_text.get()
        pyperclip.copy(generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
