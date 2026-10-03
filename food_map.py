# food_map.py

# Map: Spot -> [(Next Spot, Travel Minutes)]
MAP = {
    'Bed': [('Cabinet', 3), ('Fridge', 4)],
    'Cabinet': [('Stove', 5)],
    'Stove': [('Dinner', 4)],
    'Fridge': [('Pizza', 3), ('Freezer', 2)],
    'Pizza': [('Dinner', 1)],
    'Freezer': [('Dinner', 8)],
    'Dinner': []
}

# How close each spot feels to actual food (Heuristic)
SMELL_DISTANCE = {
    'Bed': 7,
    'Cabinet': 6,
    'Stove': 4,
    'Fridge': 4,
    'Pizza': 1,
    'Freezer': 7,
    'Dinner': 0
}