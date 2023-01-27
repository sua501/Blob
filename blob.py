from turtle import RawTurtle, Screen
import random
import math
from food import Food


class Blob(RawTurtle):
    def __init__(self, screen, v):
        super().__init__(screen)
        self.velocity = v
        self.size = 3
        self.sense = 25
        self.food_count = 0
        self.energy = 1000
        self.color(0.5 + (v - 1.5), 0.5 - abs(v - 1.5), 0.5 - (v - 1.5))
        self.shape("circle")
        self.turtlesize(0.6)
        self.penup()
        if random.choice([True, False]):
            x = random.uniform(-200, 200)
            y = random.choice([-150, 150])
        else:
            y = random.uniform(-150, 150)
            x = random.choice([-200, 200])
        self.setposition(x, y)

    def move(self, xmin, xmax, ymin, ymax):
        if self.energy == 0:
            return
        self.energy -= self.velocity ** 2
        self.left(random.uniform(-45, 45))
        self.forward(self.velocity)
        if self.xcor() < xmin:
            x = self.xcor()+(xmin-self.xcor())*2
            y = self.ycor()
            self.setposition(x, y)
        elif self.xcor() > xmax:
            x = self.xcor()-(self.xcor()-xmax)*2
            y = self.ycor()
            self.setposition(x, y)
        elif self.ycor() < ymin:
            y = self.ycor()+(ymin-self.ycor())*2
            x = self.xcor()
            self.setposition(x, y)
        elif self.ycor() > ymax:
            y = self.ycor()-(self.ycor()-ymax)*2
            x = self.xcor()
            self.setposition(x, y)

    def move_to(self, food: Food):
        x, y = self.position()
        fx, fy = food.position()
        self.setheading(math.atan2(fy-y, fx-x) / math.pi*180)
        self.forward(self.velocity)

    def find(self, foods: list[Food]):
        if len(foods) == 0:
            return False
        nearest = min(foods, key=lambda f: self.distance(f))
        distance = self.distance(nearest)
        if distance < self.size:
            self.food_count += 1
            foods.remove(nearest)
            nearest.hideturtle()
        elif distance < self.sense:
            self.move_to(nearest)
            return True
        else:
            return False

    def is_movable(self):
        if self.energy < self.velocity**2:
            return False
        else:
            return True

    def replicate(self):
        v = self.velocity
        v += random.choice([-0.1, 0.1])
        return Blob(self.screen, v)
