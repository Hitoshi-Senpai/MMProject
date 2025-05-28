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
        self.HomePage()
        
    def createPage(self):

        self.__init__(root)
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

        self.selectBtn1=tk.Button(
            self.tab1, 
            text="generate a random Image", 
            width=20,
            height=8,
            font=("Helvetica", 15),
            command=self.openFolder
        )
        self.selectBtn1.place(x=130, y=200)


        self.selectBtn2=tk.Button(
            self.tab1, 
            text="Choose an image from disk",
            width=20,
            height= 8,
            font=("Helvetica", 15),
            command=self.openFolder
        )
        self.selectBtn2.place(x=800, y=200)

        
        self.label1 =tk.Label(self.tab1, text="Image Selection Page", font=("Helvetica", 18))
        self.label1.pack(pady=10)

    def HomePage(self):
        self.greeting =tk.Label(root, text="Welcome to our game", font=("MV Boli", 22))
        self.greeting.place(x=450, y=50)

        self.developers =tk.Label(root, text="Developed by Mazen, Ahmad and Mohammad", font=("MV Boli", 15))
        self.developers.place(x=10, y=630)

        self.icon1 = tk.PhotoImage(file="icons/gear4.gif")
        self.iconLabel1 = tk.Label(root, image=self.icon1)
        self.iconLabel1.place(x=150, y=150)

        self.icon2 = tk.PhotoImage(file="icons/gear3.gif")
        self.iconLabel2 = tk.Label(root, image=self.icon2)
        self.iconLabel2.place(x=1000, y=550)


        self.startBtn=tk.Button(
            root, 
            text="Start", 
            width=14,
            height=1,
            font=("MV Boli", 17),
            command= self.createPage
        )
        self.startBtn.place(x=550, y=300)

        self.exitBtn=tk.Button(
            root, 
            text="Exit", 
            width=14,
            height=1,
            font=("MV Boli", 17),
            command= None
        )
        self.exitBtn.place(x=550, y=400)


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