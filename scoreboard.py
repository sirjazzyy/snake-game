from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCOREBOARD: {self.score} HIGHSCORE: {self.highscore}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!!", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
