from turtle import Turtle
import random

snake_coordinates = [(0, 0), (-20, 0,), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLOR = ["white", "blue", "red"]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in snake_coordinates:
            self.increase_snake(position)

    def increase_snake(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.color(random.choice(COLOR))
        tim.pu()
        tim.goto(position)
        self.segment.append(tim)

    def extend_snake(self):
        self.increase_snake(self.segment[-1].position())

    def ready(self, distance):
        self.head.fd(distance)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x_cord = self.segment[seg - 1].xcor()
            y_cord = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_cord, y_cord)
        self.ready(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
