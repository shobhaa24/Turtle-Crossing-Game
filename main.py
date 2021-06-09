import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    #detect collision with the car
    for cars in car.allcars:
        if cars.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    #detect successful crossing
    result= player.is_at_finish_line()
    if result:
        player.go_to_start()
        scoreboard.level_up()
        car.increase_speed()


screen.exitonclick()