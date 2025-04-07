import tkinter as tk
from tkinter import ttk

class NameAddressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name and Address Display")
        self.root.geometry("400x300")
        
        self.button_frame = ttk.Frame(root, padding="10")
        self.button_frame.pack(fill=tk.X)
        
        self.quit_button = ttk.Button(
            self.button_frame,
            text="Quit",
            command=root.destroy
        )
        self.quit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.display_button = ttk.Button(
            self.button_frame,
            text="Show Info",
            command=self.display_info
        )
        self.display_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.label_frame = ttk.Frame(root, padding="10")
        self.label_frame.pack(fill=tk.BOTH, expand=True)
        
        self.display_label = ttk.Label(
            self.label_frame, 
            text="", 
            font=("Arial", 12),
            wraplength=380,
            justify="center"
        )
        self.display_label.pack(pady=20)
    
    def display_info(self):
        self.display_label.config(
            text="Tucker Honeycutt\n588 Pine Grove Rd"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = NameAddressApp(root)
    root.mainloop()
