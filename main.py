from race import Race, RaceElementFactory
from utils import getBrakeConfiguration, getCategoryByAge

def createRace(age):

    categories = getCategoryByAge(age)

    if not categories:
        raise ValueError(f"No eligible categories for age {age}")

    driverDetails = {
        'raceName': 'Race1',
        'driverId': 42,
        'kartId': 7,
        'categoryId': categories[1]
    }

    race = Race(**driverDetails)
    
    lap1 = RaceElementFactory.createLap(0, 90)
    split1_1 = RaceElementFactory.createSplit(0, 30, 1)
    split1_2 = RaceElementFactory.createSplit(30, 60, 1)
    split1_3 = RaceElementFactory.createSplit(60, 90, 1)
    lap1.addSplit(split1_1)
    lap1.addSplit(split1_2)
    lap1.addSplit(split1_3)
    race.addLap(lap1)

    lap2 = RaceElementFactory.createLap(90, 180)
    split2_1 = RaceElementFactory.createSplit(90, 120, 2)
    split2_2 = RaceElementFactory.createSplit(120, 150, 2)
    split2_3 = RaceElementFactory.createSplit(150, 180, 2)
    lap2.addSplit(split2_1)
    lap2.addSplit(split2_2)
    lap2.addSplit(split2_3)
    race.addLap(lap2)

    return race

def showRaceInfo(race):
    print(f"Race: {race.raceName}, Driver: {race.driverId}, Kart: {race.kartId}, Category: {race.categoryId}, Laps: {len(race.laps)}")
    for lap in race.laps:
        print(f"Lap from {lap.lapStart} to {lap.lapEnd}")
        for split in lap.splits:
            print(f"Split from {split.splitStart} to {split.splitEnd} in lap {split.lapId}")

def configureBrakes(category, terrainCondition):
    brakes = getBrakeConfiguration(category, terrainCondition)
    print(f"Category: {category}, Terrain: {terrainCondition}, Brake Configuration: {brakes}")

def saveRaceData(race):
    filename = 'race.json'
    race.saveToFile(filename)
    print(f"Race data saved to {filename}")

def main():
    age = 30
    race = createRace(age)
    showRaceInfo(race)
    configureBrakes(race.categoryId, 'wet')
    saveRaceData(race)

if __name__ == "__main__":
    main()
