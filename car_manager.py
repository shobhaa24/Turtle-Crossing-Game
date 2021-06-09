from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.allcars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        occurence=random.randint(1, 6)
        if occurence == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y=random.randint(-250, 250)
            car.goto(300, random_y)
            self.allcars.append(car)

    def move_cars(self):
        for i in self.allcars:
            i.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


