from pprint import pprint

cars = [
    {"model": "Yaris", "make": "Toyota", "color": "red"},
    {"model": "Auris", "make": "Toyota", "color": "red"},
    {"model": "Camry", "make": "Toyota", "color": "green"},
    {"model": "Prius", "make": "Toyota", "color": "yellow"},
    {"model": "Civic", "make": "Honda", "color": "red"},
    {"model": "Model 3", "make": "Tesla", "color": "red"}
]

# filter to red cars

red_cars = []
for car in cars:
    if car['color'] == 'red':
        red_cars.append(car)


pprint(red_cars)