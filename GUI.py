import tkinter as tk
import ttkbootstrap as tb
from tkinter import filedialog
import cv2
import os
import numpy as np
from PIL import Image, ImageTk

class GUI:
    path = ""
    def __init__(self, root):
        self.root = root
        self.image1 = None
        self.image2 = None
        self.root.title("Find the Differences Game")
        self.root.geometry("1300x700")
        
        self.style = tb.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', '12'), padding=[20, 10])
        self.pathTemp = tk.StringVar()
        self.HomePage()
        
    def createPage(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.notebook = tb.Notebook(self.root, bootstyle="dark")
        self.notebook.pack(pady=20, fill=tk.BOTH, expand=True)
        
        self.tab1= tb.Frame(self.notebook)
        self.tab2= tb.Frame(self.notebook)
        
        self.tab1.pack(fill=tk.BOTH, expand=True)
        self.tab2.pack(fill=tk.BOTH, expand=True)
        
        self.notebook.add(self.tab1, text="Image Mode")
        self.notebook.add(self.tab2, text="Settings")
        
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
            command=self.gamePage
        )
        self.selectBtn1.place(x=130, y=200)


        self.selectBtn2=tk.Button(
            self.tab1, 
            text="Choose 2 images from disk",
            width=20,
            height= 8,
            font=("Helvetica", 15),
            command=self.twoImagesPage
        )
        self.selectBtn2.place(x=800, y=200)

        
        self.label1 =tk.Label(self.tab1, text="Image Selection Page", font=("Helvetica", 18))
        self.label1.pack(pady=10)

    def HomePage(self):

        for widget in self.root.winfo_children():
            widget.destroy()

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
            command= self.root.destroy
        )
        self.exitBtn.place(x=550, y=400)

    def twoImagesPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.img1Btn = tk.Button(
            root, 
            text="First Image", 
            width=12,
            height=1,
            font=("MV Boli", 14),
            command=lambda: self.openFolder(1)
        )
        self.img1Btn.place(x=170, y=150)

        self.img2Btn = tk.Button(
            root, 
            text="Second Image", 
            width=12,
            height=1,
            font=("MV Boli", 14),
            command=lambda: self.openFolder(2)
        )
        self.img2Btn.place(x=950, y=150)

        self.startGameBtn = tk.Button(
            root, 
            text="Start Game", 
            width=14,
            height=1,
            font=("MV Boli", 15),
            command=self.gamePage
        )
        self.startGameBtn.place(x=520, y=600)

        self.img1Display = tk.Label(root)
        self.img1Display.place(x=150, y=200)

        self.img2Display = tk.Label(root)
        self.img2Display.place(x=930, y=200)

    def openFolder(self, imageNum):
        imageCurrPath = filedialog.askopenfilename(
            title="Select an Image:",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        
        if imageCurrPath:
            if imageNum == 1:
                self.image1 = imageCurrPath
                displayLabel = self.img1Display
            else:
                self.image2 = imageCurrPath
                displayLabel = self.img2Display

            img = Image.open(imageCurrPath)
            img.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(img)
            
            displayLabel.config(image=photo)
            displayLabel.image = photo
                
    def resultPage(self, state = False, correctTimes =0, wrongTimes =0):

        if hasattr(self, 'notebook'):
            self.notebook.destroy()

        for widget in self.root.winfo_children():
            widget.destroy()

        msg = ""
        if state:
            msg = "Great!, You did it!! :)"
        else:
            msg = "Game Over!!"

        self.gameoverLabel =tk.Label(root, text=msg, font=("MV Boli", 45))
        self.gameoverLabel.place(x=410, y=100)

        self.scoreLabel =tk.Label(root, text=f"Your Score: {correctTimes} / {wrongTimes}", font=("MV Boli", 23))
        self.scoreLabel.place(x=470, y=300)


        self.backBtn=tk.Button(
            root, 
            text="Back", 
            width=14,
            height=1,
            font=("MV Boli", 17),
            command= self.HomePage
        )

        self.backBtn.place(x=520, y = 420)

    def gamePage(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        

        self.confirmBtn=tk.Button(
            root, 
            text="Confirm", 
            width=14,
            height=1,
            font=("MV Boli", 17),
            command= self.HomePage
        )

        self.confirmBtn.place(x=550, y=600)

        self.testBtn=tk.Button(
            root, 
            text="test result page", 
            width=15,
            height=1,
            font=("MV Boli", 10),
            command= self.resultPage
        )
        self.testBtn.place(x=50, y = 420)

# solar, vapor (▀̿Ĺ̯▀̿ ̿)
root = tb.Window(themename="vapor") 
app = GUI(root)
root.mainloop()