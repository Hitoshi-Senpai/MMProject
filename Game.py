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
            
    def getRanges(self, imgName):
        imgsRange = []
        imgsRange.append([])
        imgsRange.append([])
        imgsRange.append([[(155, 80), (180, 90)], [(230, 134), (255, 155)], [(10, 100), (60, 150)], [(350, 125), (385, 160)]])

        return imgsRange[int(imgName.split('-')[0][-1])-1]
    
    def compareRanges(self, playerRanges, imgName):
        score = 0
        missing = []
        originRanges = self.getRanges(imgName)
        for player in playerRanges:
            for origin in originRanges:
                startO, endO = origin
                startP, endP = player
                if startO == startP and endO == endP:
                    score += 1
                else:
                    missing.append(origin)
        return (score, missing), 

        
        