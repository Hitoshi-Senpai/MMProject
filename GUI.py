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
        self.user_answers = []
        self.tempMovements = []
        self.annotations = []

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

    def check_result(self):
        correct_count = 0
        matched = [False] * len(self.correct_answers)

        for ux, uy in self.user_answers:
            for idx, ((x1, y1), (x2, y2)) in enumerate(self.correct_answers):
                if not matched[idx] and x1 <= ux <= x2 and y1 <= uy <= y2:
                    correct_count += 1
                    matched[idx] = True
                    break

        total = len(self.correct_answers)
        self.resultPage(state=(correct_count == total), correctTimes=correct_count, wrongTimes=total)

    def canvas2_click(self, event):
        x, y = event.x, event.y
        shape = self.selected_shape.get()
        shapeId = None
        size = 30  # "temp"
        coords = (x - size, y - size, x + size, y + size)

        if shape == "circle":
            shapeId = self.canvas2.create_oval(
                coords,
                outline="red", width=2
            )
        elif shape == "rectangle":
            shapeId = self.canvas2.create_rectangle(
                coords,
                outline="blue", width=2
            )

        if shapeId:
            self.annotations.append((shape,coords,shapeId))
            self.user_answers.append((x,y))
            self.tempMovements.clear()
    def redo(self):
        if self.tempMovements:
            shapeType, coords,shapeId= self.tempMovements.pop()
            shapeId = None
            if shapeType == "circle":
                shapeId = self.canvas2.create_oval(
                    coords,
                    outline="red",width=2
                )
            elif shapeType == "rectangle":
                shapeId = self.canvas2.create_rectangle(
                    coords,
                    outline="blue",width=2
                )
            if shapeId:
                self.annotations.append((shapeType,coords,shapeId))
                xCenter = (coords[0] + coords[2])/2
                yCenter = (coords[1] + coords[3])/2
                self.user_answers.append((xCenter,yCenter))

    def undo(self):
        if self.annotations:
            shape = self.annotations.pop()
            shapeStyle,coords,shapeId = shape
            self.canvas2.delete(shapeId)
            self.tempMovements.append(shape)
            if self.user_answers:
                self.user_answers.pop()

    def gamePage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.correct_answers = [ #########just for testing :\ #########
            [(100, 100), (150, 150)],
            [(300, 250), (340, 290)],
        ]

        self.root.geometry("1300x700")

        self.confirmBtn = tk.Button(
            self.root,
            text="Confirm",
            width=14,
            height=1,
            font=("MV Boli", 17),
            command=self.HomePage
        )
        self.confirmBtn.place(x=550, y=600)

        self.testBtn = tk.Button(
            self.root,
            text="test result page",
            width=15,
            height=1,
            font=("MV Boli", 10),
            command=self.check_result
        )
        self.testBtn.place(x=50, y=420)

        self.selected_shape = tk.StringVar(value= "rectangle")
        shape_label = tk.Label(self.root, text="Select shape:", font=("MV Boli", 12))
        shape_label.place(x=850, y=550)

        shape_menu = tk.OptionMenu(self.root, self.selected_shape, "rectangle", "circle")
        shape_menu.config(font=("MV Boli", 12), width=10)
        shape_menu.place(x=1000, y=550)

        self.undoBtn = tk.Button(
            self.root,
            text="Undo",
            width=14,
            height=1,
            font=("MV Boli", 10),
            command=self.undo
        )
        self.undoBtn.place(x=50, y=600)
        self.redoBtn = tk.Button(
            self.root,
            text="Redo",
            width=14,
            height=1,
            font=("MV Boli", 10),
            command=self.redo
        )
        self.redoBtn.place(x=50, y=650)
        if self.image1 and self.image2:
            img1 = Image.open(self.image1).resize((400, 400), Image.Resampling.LANCZOS)
            img2 = Image.open(self.image2).resize((400, 400), Image.Resampling.LANCZOS)

            self.tk_img1 = ImageTk.PhotoImage(img1)
            self.tk_img2 = ImageTk.PhotoImage(img2)

            self.canvas1 = tk.Canvas(self.root, width=400, height=400)
            self.canvas1.place(x=250, y=100)
            self.canvas1.create_image(0, 0, anchor="nw", image=self.tk_img1)

            self.canvas2 = tk.Canvas(self.root, width=400, height=400)
            self.canvas2.place(x=700, y=100)
            self.canvas2.create_image(0, 0, anchor="nw", image=self.tk_img2)


            self.canvas2.bind("<Button-1>",self.canvas2_click)
        else:
            tk.messagebox.showerror("Error", "Please select two images first.")


# solar, vapor (▀̿Ĺ̯▀̿ ̿)
root = tb.Window(themename="vapor")
app = GUI(root)
root.mainloop()