from turtle import RawTurtle, Screen
import random


class Food(RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)
        self.size = 5
        self.color("orange")
        self.shape("circle")
        self.turtlesize(0.3)
        self.penup()

        x = random.uniform(-200, 200)
        y = random.uniform(-150, 150)
        self.setposition(x, y)
