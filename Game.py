import random

class Game:
    def __init__(self):
        self.history = set()

    def getImagePairs(self):
        if len(self.history) == 3:
            self.history.clear()
        while True:
            index = random.randint(1, 3)
            if index not in self.history:
                self.history.add(index)
                return (f"Images/img{index}-1.png", f"Images/img{index}-2.png")
            
    def getRanges(imgName):
        k1=[[(236,604),(38,651)],[(249,670),(476,546)],[(140,60),(271,132)],[(135,180),(499,243)],[(19,392),(83,494)]]
        k2=[[(106,56),(231,243)],[(57,501),(229,576)],[(383,556),(477,669)]]
        
        # bruh dog shit ):
        return None
        