from turtle import Screen, RawTurtle
from blob import Blob
from food import Food


class World:
    def __init__(self, width, height):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.blobs: list[Blob] = []
        self.foods: list[Food] = []
        self.radius = 200
        self.field_xmin = -(width/2)
        self.field_xmax = (width/2)
        self.field_ymin = -(height/2)
        self.field_ymax = (height/2)
        self.reporter = RawTurtle(self.screen)
        self.reporter.color("white")
        self.reporter.hideturtle()
        self.reporter.penup()
        self.reporter.setposition(-self.screen.window_width() / 2.5, -180)

    def draw_circle(self):
        drawer = RawTurtle(self.screen)
        drawer.hideturtle()
        drawer.penup()
        drawer.forward(self.radius)
        drawer.left(90)
        drawer.pendown()
        drawer.circle(self.radius)

    def draw_rect(self, width, height):
        drawer = RawTurtle(self.screen)
        drawer.pencolor("white")
        drawer.hideturtle()
        drawer.penup()
        drawer.left(90)
        drawer.forward(height/2)
        drawer.left(90)
        drawer.pendown()
        drawer.forward(width/2)
        drawer.left(90)
        drawer.forward(height)
        drawer.left(90)
        drawer.forward(width)
        drawer.left(90)
        drawer.forward(height)
        drawer.left(90)
        drawer.forward(width/2)

    def start(self):
        v = 1.5
        #float(input("속도 입력: "))
        for _ in range(30):
            self.blobs.append(Blob(self.screen, v))

        self.screen.tracer(False)
        while True:
            self.turn()
            self.reporter.clear()
            self.reporter.write(
                f"\rNumber of Blob = {len(self.blobs)}",
                font=("Terminal", 17, "normal"),
            )

    def turn(self):
        for food in self.foods:
            food.hideturtle()
        self.foods.clear()
        for _ in range(30):
            self.foods.append(Food(self.screen))
        for blob in self.blobs:
            blob.energy = 1500
            blob.food_count = 0
        while 1:
            xx = 0
            for i in range(len(self.blobs)):
                if self.blobs[i].is_movable() == True:
                    break
                else:
                    xx += 1
            if xx == len(self.blobs):
                break
            for i in range(len(self.blobs)):
                if self.blobs[i].find(self.foods) == False:
                    if self.blobs[i].is_movable() == True:
                        self.blobs[i].move(
                            self.field_xmin, self.field_xmax, self.field_ymin, self.field_ymax)
            self.screen.update()

        for blob in self.blobs:
            if blob.food_count == 0:
                blob.hideturtle()
                self.blobs.remove(blob)
            elif blob.food_count > 1:
                self.blobs.append(blob.replicate())


if __name__ == "__main__":
    world = World(400, 300)
    world.draw_rect(400, 300)
    world.start()
