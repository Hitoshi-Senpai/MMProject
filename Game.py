import random

class Game:
    def __init__(self):
        self.history = set()
        self.imgsRange = []
        self.storeRanges()

    def storeRanges(self):
        self.imgsRange.append([[(235, 150), (285, 222)], [(100, 350), (130, 375)], [(30, 470),(85, 433)], [(474, 465), (510, 415)], [(470, 80), (550, 130)],[(100, 170),(150, 190)]])
        self.imgsRange.append([[(20, 350), (50, 381)]])
        self.imgsRange.append([[(155, 80), (180, 90)], [(230, 134), (255, 155)], [(10, 100), (60, 150)], [(350, 125), (385, 160)], [(264, 106), (292, 120)]])


    def getImagePairs(self):
        if len(self.history) == 3:
            self.history.clear()
        while True:
            index = random.randint(1, 3)
            if index not in self.history:
                self.history.add(index)
                return (f"Images/img{index}-1.png", f"Images/img{index}-2.png")
    
    def getRangeLength(self, imgName):
        index = self.getNumOfImage(imgName)
        return len(self.imgsRange[index])
    
    def getNumOfImage(self, imgName):
        return int(imgName.split('-')[0][-1])-1

    def getRanges(self, imgName):
        return self.imgsRange[self.getNumOfImage(imgName)]
    
    def compareRanges(self, playerRanges, imgName):
        score = 0
        missing = []
        originRanges = self.getRanges(imgName)

        for origin in originRanges:
            ostart, oend = origin
            inRange= False
            
            for player in playerRanges:
                pstart, pend = player
                
                if not (pend[0] < ostart[0] or  
                        pstart[0] > oend[0] or   
                        pend[1] < ostart[1] or 
                        pstart[1] > oend[1]): 
                    score += 1
                    inRange = True
                    break
                    
            if not inRange:
                missing.append(origin)
        return (score, missing)
                
                