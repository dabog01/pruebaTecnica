class Race:
    def __init__(self, raceName, driverId, kartId, categoryId):
        self.raceName = raceName
        self.driverId = driverId
        self.kartId = kartId
        self.categoryId = categoryId
        self.laps = []

    def addLap(self, lap):
        self.laps.append(lap)

class Lap:
    def __init__(self, lapStart, lapEnd):
        self.lapStart = lapStart
        self.lapEnd = lapEnd
        self.splits = []

    def addSplit(self, split):
        self.splits.append(split)

class Split:
    def __init__(self, splitStart, splitEnd):
        self.splitStart = splitStart
        self.splitEnd = splitEnd
