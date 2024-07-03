import json

class Race:
    def __init__(self, raceName, driverId, kartId, categoryId):
        self.raceName = raceName
        self.driverId = driverId
        self.kartId = kartId
        self.categoryId = categoryId
        self.laps = []

    def addLap(self, lap):
        self.laps.append(lap)

    def saveRace(self):
        raceData = {
            'raceName': self.raceName,
            'driverId': self.driverId,
            'kartId': self.kartId,
            'categoryId': self.categoryId,
            'laps': []
        }
        for lap in self.laps:
            lapData = {
                'lapStart': lap.lapStart,
                'lapEnd': lap.lapEnd,
                'splits': []
            }
            for split in lap.splits:
                splitData = {
                    'splitStart': split.splitStart,
                    'splitEnd': split.splitEnd,
                    'lapId': split.lapId
                }
                lapData['splits'].append(splitData)
            raceData['laps'].append(lapData)
        return raceData

    def saveToFile(self, filename):
        raceData = self.saveRace()
        with open(filename, 'w') as file:
            json.dump(raceData, file, indent=4)

class Lap:
    def __init__(self, lapStart, lapEnd):
        self.lapStart = lapStart
        self.lapEnd = lapEnd
        self.splits = []

    def addSplit(self, split):
        self.splits.append(split)

class Split:
    def __init__(self, splitStart, splitEnd, lapId):
        self.splitStart = splitStart
        self.splitEnd = splitEnd
        self.lapId = lapId
