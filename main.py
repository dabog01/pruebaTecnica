from race import Race, Lap, Split
from utils import getBrakeConfiguration, getCategoryByAge

def main():
    age = 30
    categories = getCategoryByAge(age)
    print(f"Driver age: {age}, Eligible categories: {categories}")

    race = Race("Race1", 1, 1, 1)
    lap = Lap(0, 100)
    lap.addSplit(Split(0, 50))
    lap.addSplit(Split(50, 100))
    race.addLap(lap)

    # Mostrar información de la carrera
    print(f"Race: {race.raceName}, Driver: {race.driverId}, Kart: {race.kartId}, Category: {race.categoryId}, Laps: {len(race.laps)}")
    for lap in race.laps:
        print(f"Lap from {lap.lapStart} to {lap.lapEnd}")
        for split in lap.splits:
            print(f"Split from {split.splitStart} to {split.splitEnd}")

    category = 'DD2'
    terrainCondition = 'dry'
    brakes = getBrakeConfiguration(category, terrainCondition)
    print(f"Category: {category}, Terrain: {terrainCondition}, Brake Configuration: {brakes}")

if __name__ == "__main__":
    main()
