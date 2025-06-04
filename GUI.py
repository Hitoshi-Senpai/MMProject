import tkinter as tk
import ttkbootstrap as tb
from tkinter import filedialog
import cv2
import os
import winsound
import numpy as np
from PIL import Image, ImageTk
from Game import Game

class GUI:
    path = ""

    def __init__(self, root):
        self.root = root
        self.image1 = None
        self.image2 = None
        self.annotations = []
        self.playerShapes = []
        self.root.title("Find the Differences Game")
        self.root.geometry("1300x700")
        self.game = Game()
        self.clicks=0
        self.labelClicks = tk.Label(root, text=f"{self.clicks}", bg="black", font=("MV Boli", 20), fg="green")

        self.style = tb.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', '12'), padding=[20, 10])
        self.pathTemp = tk.StringVar()
        self.HomePage()
        self.userAnswers = []
        self.tempMovements = []

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

        def selectBtnAction():
            self.image1, self.image2 = self.game.getImagePairs()
            self.gamePage()

        self.selectBtn1=tk.Button(
            self.tab1, 
            text="generate a random Image", 
            width=20,
            height=8,
            font=("Helvetica", 15),
            command=selectBtnAction
        )
        self.selectBtn1.place(x=130, y=200)

        def selectBtnAction():
            self.image1, self.image2 = self.game.getImagePairs()
            self.gamePage()

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

        self.playerShapes.clear()

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
                
    def resultPage(self, state=False, correctTimes=0, allTimes=0, missing_ranges=None, image1=None, image2=None):
        if hasattr(self, 'notebook'):
            self.notebook.destroy()

        
        for widget in self.root.winfo_children():
            widget.destroy()

        
        msg = "Great!, You did it!! :)" if state else "Game Over!!"
        self.gameoverLabel = tk.Label(self.root, text=msg, font=("MV Boli", 30))
        self.gameoverLabel.place(relx=0.5, y=10, anchor="n")

        
        self.scoreLabel = tk.Label(self.root, text=f"Your Score: {correctTimes} / {allTimes}", font=("MV Boli", 18))
        self.scoreLabel.place(relx=0.5, y=75, anchor="n")

        
        self.backBtn = tk.Button(
            self.root,
            text="Back",
            width=14,
            height=1,
            font=("MV Boli", 17),
            command=self.HomePage
        )
        self.backBtn.place(relx=0.1, rely=0.9, anchor="n")

        
        if image1 and image2:
            
            img1 = Image.open(image1).resize((400, 400), Image.Resampling.LANCZOS)
            img2 = Image.open(image2).resize((400, 400), Image.Resampling.LANCZOS)

            
            self.tkImg1 = ImageTk.PhotoImage(img1)
            self.tkImg2 = ImageTk.PhotoImage(img2)

            
            origW, origH = Image.open(image2).size
            dispW, dispH = (400, 400)

            
            scaleX = dispW / origW
            scaleY = dispH / origH

            originRanges = self.game.getRanges(image2)

            
            self.canvas1 = tk.Canvas(self.root, width=dispW, height=dispH)
            self.canvas1.place(x=250, y=150)
            self.canvas1.create_image(0, 0, anchor="nw", image=self.tkImg1)

            self.canvas2 = tk.Canvas(self.root, width=dispW, height=dispH)
            self.canvas2.place(x=700, y=150)
            self.canvas2.create_image(0, 0, anchor="nw", image=self.tkImg2)

            correct_origins = []
            if missing_ranges:
                for origin in originRanges:
                    if origin not in missing_ranges:
                        correct_origins.append(origin)
            else:
                correct_origins=originRanges
            
            if missing_ranges:
                for origin in missing_ranges:
                    
                    (x1_orig, y1_orig), (x2_orig, y2_orig) = origin

                    
                    x1_scaled = int(x1_orig * scaleX)
                    y1_scaled = int(y1_orig * scaleY)
                    x2_scaled = int(x2_orig * scaleX)
                    y2_scaled = int(y2_orig * scaleY)

                   
                    self.canvas2.create_rectangle(
                        x1_scaled, y1_scaled,
                        x2_scaled, y2_scaled,
                        outline="red", width=3
                    )
            for origin in correct_origins:
                (x1_o, y1_o), (x2_o, y2_o) = origin
                x1_g = int(x1_o * scaleX)
                y1_g = int(y1_o * scaleY)
                x2_g = int(x2_o * scaleX)
                y2_g = int(y2_o * scaleY)

                
                self.canvas2.create_rectangle(
                    x1_g, y1_g, x2_g, y2_g,
                    outline="#39FF14"
                    , width=3
                )
        

        else:
            tk.messagebox.showerror("Error", "Please select two images first.")
                
    def confirmBtnAction(self):
            print(self.playerShapes)
            score, mis = self.game.compareRanges(self.playerShapes, self.image1)
            state = False
            if len(mis) == 0:
                state = True
            self.resultPage(state, score, len(mis)+score,mis,self.image1,self.image2)

    def canvas2Click(self, event):   
        if self.clicks>=7:
            return
        self.clicks+=1
        self.labelClicks.config(text=f"{self.clicks}")

        if self.clicks==7:
            self.confirmBtnAction()
        elif self.clicks==6:
                winsound.Beep(1000, 500)


        scaleX = self.originalSize[0] / self.displayedSize[0]
        scaleY = self.originalSize[1] / self.displayedSize[1]
        
        originalX = event.x * scaleX
        originalY = event.y * scaleY
        
        size = 30 * scaleX 
        coords = (originalX - size, originalY - size, 
                originalX + size, originalY + size)
        
        shape = self.selectedShape.get()
        shapeId = None

        displayCoords = (event.x - 30, event.y - 30, 
                        event.x + 30, event.y + 30)
        
        if shape == "circle":
            shapeId = self.canvas2.create_oval(
                displayCoords, outline="red", width=2
            )
        elif shape == "rectangle":
            shapeId = self.canvas2.create_rectangle(
                displayCoords, outline="blue", width=2
            )

        if shapeId:
            self.annotations.append((shape, displayCoords, shapeId))
            self.playerShapes.append([(coords[0], coords[1]), (coords[2], coords[3])])
            self.userAnswers.append((originalX, originalY))
            self.tempMovements.clear()

        



    def redo(self):
        if self.tempMovements:
            shapeType, coords, _ = self.tempMovements.pop()
            shapeId = None
            scaleX = self.originalSize[0] / self.displayedSize[0]
            scaleY = self.originalSize[1] / self.displayedSize[1]

            originalCoords = (
                coords[0] * scaleX,
                coords[1] * scaleY,
                coords[2] * scaleX,
                coords[3] * scaleY
            )

            if shapeType == "circle":
                shapeId = self.canvas2.create_oval(coords, outline="red", width=2)
            elif shapeType == "rectangle":
                shapeId = self.canvas2.create_rectangle(coords, outline="blue", width=2)

            if shapeId:
                self.annotations.append((shapeType, coords, shapeId))
                self.playerShapes.append([(originalCoords[0], originalCoords[1]),
                                          (originalCoords[2], originalCoords[3])])
                xCenter = (originalCoords[0] + originalCoords[2]) / 2
                yCenter = (originalCoords[1] + originalCoords[3]) / 2
                self.userAnswers.append((xCenter, yCenter))

            self.clicks += 1
            self.labelClicks.config(text=f"{self.clicks}")

    def undo(self):
        if self.annotations:
            shape = self.annotations.pop()
            shapeStyle, coords, shapeId = shape
            self.canvas2.delete(shapeId)
            self.tempMovements.append(shape)

            if self.userAnswers:
                self.userAnswers.pop()

            if self.clicks > 0:
                self.clicks -= 1
                self.labelClicks.config(text=f"{self.clicks}")

    def gamePage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.clicks = 0
        self.annotations = []
        self.playerShapes = []
        self.userAnswers = []
        self.tempMovements = []

        self.correctAnswers = [
            [(100, 100), (150, 150)],
            [(300, 250), (340, 290)],
        ]

        def countdown(seconds):
            mins = seconds // 60
            secs = seconds % 60
            if seconds == 10 and mins == 0:
                winsound.Beep(1000, 500)

            timeText = f"{mins}:{secs:02}"
            if seconds <= 10 and mins == 0 and seconds != 0:
                labelTimer.config(text=timeText, fg="red")
            elif seconds == 0:
                labelTimer.config(text="Time is up!", fg="red")
                self.confirmBtnAction()
            else:
                labelTimer.config(text=timeText)

            self.root.after(1000, countdown, seconds - 1)

        self.root.geometry("1300x700")

        self.labelClicks = tk.Label(self.root, text=f"{self.clicks}", font=("MV Boli", 16), fg="black")
        self.labelClicks.place(relx=0.8, rely=0.01, anchor="n")

        self.confirmBtn = tk.Button(self.root, text="Confirm", width=14, height=1, font=("MV Boli", 17),
                                    command=self.confirmBtnAction)
        self.confirmBtn.place(x=550, y=600)

        self.selectedShape = tk.StringVar(value="rectangle")

        shapeLabel = tk.Label(self.root, text="Select shape:", font=("MV Boli", 12))
        shapeLabel.place(x=850, y=550)

        shapeMenu = tk.OptionMenu(self.root, self.selectedShape, "rectangle", "circle")
        shapeMenu.config(font=("MV Boli", 12), width=10)
        shapeMenu.place(x=1000, y=550)

        self.undoBtn = tk.Button(self.root, text="Undo", width=14, height=1, font=("MV Boli", 10),
                                 command=self.undo)
        self.undoBtn.place(x=50, y=600)

        self.redoBtn = tk.Button(self.root, text="Redo", width=14, height=1, font=("MV Boli", 10),
                                 command=self.redo)
        self.redoBtn.place(x=50, y=650)

        if self.image1 and self.image2:
            img1 = Image.open(self.image1).resize((400, 400), Image.Resampling.LANCZOS)
            img2 = Image.open(self.image2).resize((400, 400), Image.Resampling.LANCZOS)
            self.tkImg1 = ImageTk.PhotoImage(img1)
            self.tkImg2 = ImageTk.PhotoImage(img2)

            self.originalSize = Image.open(self.image2).size
            self.displayedSize = (400, 400)

            self.canvas1 = tk.Canvas(self.root, width=400, height=400)
            self.canvas1.place(x=250, y=100)
            self.canvas1.create_image(0, 0, anchor="nw", image=self.tkImg1)

            self.canvas2 = tk.Canvas(self.root, width=400, height=400)
            self.canvas2.place(x=700, y=100)
            self.canvas2.create_image(0, 0, anchor="nw", image=self.tkImg2)

            self.canvas2.bind("<Button-1>", self.canvas2Click)
        else:
            tk.messagebox.showerror("Error", "Please select two images first.")

        labelTimer = tk.Label(self.root, text="5:00", bg="black", font=("MV Boli", 20), fg="green")
        labelTimer.place(relx=0.5, rely=0.01, anchor="n")

        countdown(30)

   
# solar, vapor (▀̿Ĺ̯▀̿ ̿)
root = tb.Window(themename="vapor")
app = GUI(root)
root.mainloop()