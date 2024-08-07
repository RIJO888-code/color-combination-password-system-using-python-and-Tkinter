import tkinter as tk
from tkinter import messagebox



class ColorPasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Password System")

       
        self.colors = {
            "Red": "#FF0000",
            "Green": "#00FF00",
            "Blue": "#0000FF",
            "Yellow": "#FFFF00",
            "Cyan": "#00FFFF",
            "Magenta": "#FF00FF",
            "Orange": "#FFA500",
            "Purple": "#800080",
            "Pink": "#FFC0CB",
            "Brown": "#A52A2A",
            "Gray": "#808080",
            "Black": "#000000",
            "White": "#FFFFFF",
            "LightBlue": "#ADD8E6",
            "DarkGreen": "#006400",
            "Gold": "#FFD700",
            "Silver": "#C0C0C0",
            "Teal": "#008080",
            "Lavender": "#E6E6FA",
            "Coral": "#FF7F50"
        }
        self.color_sequence = []
        self.password = []

        # Setup UI
        self.create_color_matrix()
        self.create_buttons()

    def create_color_matrix(self):
       
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        
        for idx, (color_name, color_code) in enumerate(self.colors.items()):
            button = tk.Button(frame, bg=color_code, width=10, height=3,
                               command=lambda c=color_name: self.select_color(c))
            button.grid(row=idx // 4, column=idx % 4)  

    def create_buttons(self):
       
        self.set_password_button = tk.Button(self.root, text="Set Password", command=self.set_password)
        self.set_password_button.pack(pady=5)

        
        self.verify_password_button = tk.Button(self.root, text="Verify Password", command=self.verify_password)
        self.verify_password_button.pack(pady=5)

        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

    def select_color(self, color_name):
       
        if len(self.color_sequence) < 5:
            self.color_sequence.append(color_name)
        else:
            messagebox.showinfo("Info", "You can only select up to 5 colors.")

    def set_password(self):
        
        if len(self.color_sequence) < 4:
            messagebox.showerror("Error", "Password must be at least 4 colors long.")
        else:
            self.password = self.color_sequence.copy()
            self.color_sequence.clear()
            messagebox.showinfo("Info", "Password set successfully.")

    def verify_password(self):
        
        if self.color_sequence == self.password:
            messagebox.showinfo("Success", "Password verified successfully.")
        else:
            messagebox.showerror("Error", "Incorrect password.")
        self.color_sequence.clear()

    def reset(self):
        
        self.color_sequence.clear()
        self.password.clear()
        messagebox.showinfo("Info", "Reset successfully.")



root = tk.Tk()
app = ColorPasswordApp(root)
root.mainloop()
