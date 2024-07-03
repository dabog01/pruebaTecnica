def getBrakeConfiguration(category, terrainCondition):
    
    brakeConfiguration = {
        'DD2': {
            'dry': {'front': 0, 'rear': 100},
            'wet': {'front': 70, 'rear': 40}
        },
        'DD2Master': {
            'dry': {'front': 0, 'rear': 100},
            'wet': {'front': 70, 'rear': 40}
        },
        'Junior': {
            'dry': {'front': 0, 'rear': 100},
            'wet': {'front': 70, 'rear': 40}
        }
    }

    if category not in brakeConfiguration:
        return "Unknown category"
    
    if terrainCondition not in brakeConfiguration[category]:
        return "Unknown terrain condition"

    return brakeConfiguration[category][terrainCondition]

def getCategoryByAge(age):
    if age > 25:
        return ['DD2', 'DD2Master']
    elif 18 <= age <= 25:
        return ['Junior']
    else:
        return []
