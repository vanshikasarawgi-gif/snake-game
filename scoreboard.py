from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score= int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score} ", align="center", font=("Arial", 13, "bold"))

    def count_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("Game Over ", align="center", font=("Arial", 30, "bold"))






