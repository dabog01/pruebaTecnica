from race import Race, Lap, Split
from util import getBrakeConfiguration, getCategoryByAge

def main():
    age = int(input("Enter the driver's age: "))
    categories = getCategoryByAge(age)
    print(f"Driver age: {age}, Eligible categories: {categories}")

    if not categories:
        print("No eligible categories for the given age.")
        return

    raceName = input("Enter the race name: ")
    driverId = int(input("Enter the driver ID: "))
    kartId = int(input("Enter the kart ID: "))
    categoryId = input("Enter the category ID: ")

    race = Race(raceName, driverId, kartId, categoryId)

    addMoreLaps = 'yes'
    while addMoreLaps.lower() == 'yes':
        lapStart = int(input("Enter the lap start time: "))
        lapEnd = int(input("Enter the lap end time: "))
        lap = Lap(lapStart, lapEnd)

        addMoreSplits = 'yes'
        while addMoreSplits.lower() == 'yes':
            splitStart = int(input("Enter the split start time: "))
            splitEnd = int(input("Enter the split end time: "))
            lapId = len(race.laps) + 1
            split = Split(splitStart, splitEnd, lapId)
            lap.addSplit(split)
            addMoreSplits = input("Add another split? (yes/no): ")

        race.addLap(lap)
        addMoreLaps = input("Add another lap? (yes/no): ")

    # Mostrar información de la carrera
    print(f"Race: {race.raceName}, Driver: {race.driverId}, Kart: {race.kartId}, Category: {race.categoryId}, Laps: {len(race.laps)}")
    for lap in race.laps:
        print(f"Lap from {lap.lapStart} to {lap.lapEnd}")
        for split in lap.splits:
            print(f"Split from {split.splitStart} to {split.splitEnd} in lap {split.lapId}")

    # Mostrar configuración de frenos
    category = input("Enter the category for brake configuration: ")
    terrainCondition = input("Enter the terrain condition (dry/wet): ")
    brakes = getBrakeConfiguration(category, terrainCondition)
    print(f"Category: {category}, Terrain: {terrainCondition}, Brake Configuration: {brakes}")

    # Guardar la información de la carrera
    filename = input("Enter the filename to save the race data (e.g., race_data.json): ")
    race.saveToFile(filename)
    print(f"Race data saved to {filename}")

if __name__ == "__main__":
    main()
