import tkinter as tk
import ttkbootstrap as tb
from tkinter import filedialog
import cv2
import os
import numpy as np

class GUI:
    path = ""
    def __init__(self, root):
        self.root = root
        self.image = None
        self.root.title("Image App")
        self.root.geometry("1300x700")
        
        self.style = tb.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', '12'), padding=[20, 10])
        self.pathTemp = tk.StringVar()
        self.createPage()
        
    def createPage(self):
        self.notebook = tb.Notebook(self.root, bootstyle="dark")
        self.notebook.pack(pady=20, fill=tk.BOTH, expand=True)
        
        self.tab1= tb.Frame(self.notebook)
        self.tab2= tb.Frame(self.notebook)
        
        self.tab1.pack(fill=tk.BOTH, expand=True)
        self.tab2.pack(fill=tk.BOTH, expand=True)
        
        self.notebook.add(self.tab1, text="Image Tab")
        self.notebook.add(self.tab2, text="converting Tab")
        
        self.imageTab()
    
    def imageTab(self):

        self.icon1 = tk.PhotoImage(file="icons/gear1.gif")
        iconLabel = tk.Label(self.tab1, image=self.icon1)
        iconLabel.pack(pady=10)

        self.style.configure(
            'LargeFont.TButton',
            font=('Helvetica', 20),
            padding=(0, 5),
            anchor='center'
        )

        self.selectBtn1=tk.Button(
            self.tab1, 
            text="generate a random Image", 
            width=20,
            height=8,
            font=("Helvetica", 15),
            # state='LargeFont.TButton',
            command=self.openFolder
        )
        self.selectBtn1.place(x=130, y=200)


        self.selectBtn2=tk.Button(
            self.tab1, 
            text="Choose an image from disk",
            # bootstyle="success",
            width=20,
            height= 8,
            # state='LargeFont.TButton',
            font=("Helvetica", 15),
            command=self.openFolder
        )
        self.selectBtn2.place(x=800, y=200)

        
        self.label1 =tk.Label(self.tab1, text="Image Selection Page", font=("Helvetica", 18))
        self.label1.pack(pady=10)



    def openFolder(self):
        self.image = filedialog.askopenfilename(
            title="Select an Image:",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        
        if self.image:
            self.textArea.delete("1.0", tk.END)
            self.textArea.insert(tk.END, f"Selected Image Path:\n{self.image}\n\n")
            self.textArea.insert(tk.END, f"Image successfully selected (:")
            self.pathTemp.set(self.image)



root = tb.Window(themename="superhero")
app = GUI(root)
root.mainloop()