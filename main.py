import turtle

Window = turtle.Screen()
Window.title("MAZE GAME (LEVEL 1)")
Window.setup(700, 700)
turtle.register_shape("wall2.gif")
turtle.register_shape("dleft.gif")
turtle.register_shape("dright.gif")
turtle.register_shape("mb.gif")


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wall2.gif")
        self.penup()
        self.speed(0)


class Dog(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("dright.gif")
        self.penup()
        self.speed(0)

    def go_up(self):
        if (self.xcor(), self.ycor() + 24) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)
            if (self.xcor(), self.ycor()) in final:
                Window.clearscreen()
                main()

    def go_down(self):
        if (self.xcor(), self.ycor() - 24) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)
            if (self.xcor(), self.ycor()) in final:
                Window.clearscreen()
                main()

    def go_left(self):
        if (self.xcor() - 24, self.ycor()) not in walls:
            self.shape("dleft.gif")
            self.goto(self.xcor() - 24, self.ycor())
            if (self.xcor(), self.ycor()) in final:
                Window.clearscreen()
                main()

    def go_right(self):
        if (self.xcor() + 24, self.ycor()) not in walls:
            self.shape("dright.gif")
            self.goto(self.xcor() + 24, self.ycor())
            if (self.xcor(), self.ycor()) in final:
                Window.clearscreen()
                main()


class Bone(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mb.gif")
        self.penup()
        self.speed(0)


level_4 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "XP                      X",
           "X XXXXXX XXXXX XXXXX XXXX",
           "X      X XXXXX     X XXXX",
           "XXXXXX X XXXXXXXXX X   XX",
           "X    X X       X   XXX XX",
           "X XX   XXXXXXX X XX    XX",
           "X XXXXXXXXXXXX X XX XX XX",
           "X XXXX       X X XX XX  X",
           "X      XXX XXX X XX     X",
           "X XXXXXXXX X   X X    X X",
           "X XXX      X XXXXXXXX X X",
           "X XXX XXX XX XXXXXXXX X X",
           "X XXX XXX XX      XXX X X",
           "XX    XXX XXXXXXX     X X",
           "XX XXXXXXXXX      X XXX X",
           "XX        XX XXXXXX XXX X",
           "XX XXXXXX XX XXXXXX XXX X",
           "XX    XXX XX      X     X",
           "XXXXXXXXX XXXXXXX XXXX XX",
           "XX        X    XX X XX XX",
           "XX XXXXXXXX XX XX X X  XX",
           "XX XXXXXXXXXXX    X    XX",
           "XX        EXXXXXXXXXXX XX",
           "XXXXXXXXXXXXXXXXXXXXXXXXX"]

level_2 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "XP                      X",
           "X XX XX XXXXXXXXXXXX XX X",
           "X XX XX           XX XX X",
           "X XX XXXXXXXXXXXX XX XX X",
           "X               X XX XX X",
           "XX XX XX XXXXXX X XX X  X",
           "XX XX XX XXXXXX X XX X XX",
           "XX            X X XX X XX",
           "XXXXXXXX XXXXXX X X  X XX",
           "X               X X XX XX",
           "XXXX XXXXXXX XXXX X XX XX",
           "X                 X XX XX",
           "XXX XXX XXXXXXXXXXX XX XX",
           "XXX XXX XXX     X   XX XX",
           "XXX XXX XXX XXX X      XX",
           "XXX XXXXXXX XXX X XXXX XX",
           "XXX         XXX X X    XX",
           "XXXXXXX XXXXXXXXX X XX XX",
           "X           X     X XX XX",
           "X XXX XXXX XXX XXXX XX XX",
           "X XXX XXXX XXXXXXX  XXXXX",
           "X XXX XXXX  X    X XXXXXX",
           "X XXX       X          EX",
           "XXXXXXXXXXXXXXXXXXXXXXXXX"]

level_3 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "XP                      X",
           "XXX XXXXXXXX XXX XXXXXX X",
           "XXX X        XXX XX     X",
           "XXX X XXXXXXXXXX X   X  X",
           "X   X X          X X XXXX",
           "X X X X X XXXXXXXX X XXXX",
           "X X X X X       XX X XXXX",
           "X XXX X X XXXXX XX X XXXX",
           "X     X X X   X XX X XXXX",
           "XXX XXX X X X   XXXXX   X",
           "X X X   XXX XXXXXXXXXXX X",
           "X X X XXXXX X         X X",
           "X X X    XX   XXXXX X X X",
           "X X XX X XXXXXXXXXX X X X",
           "X X XX X    XX      X X X",
           "X X XX XXXXXXXX XXXXX X X",
           "X       X       XXXXXXX X",
           "XX XX X X XX XX XX      X",
           "XX XX X X XX XX XX XXX XX",
           "X  XX X X XX XXXXX XXX XX",
           "XX     XXXXX XX    XXX XX",
           "XXXXXXX      XX XXXXXX XX",
           "XE       XXXXXX        XX",
           "XXXXXXXXXXXXXXXXXXXXXXXXX"]

level_1 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "XP                      X",
           "X XXXXXXXX XXXXXX XXXXX X",
           "X        X X    X X   X X",
           "XXXXXXXX X X XX X X X X X",
           "X      X X X XX X X X X X",
           "X XXXX X X X XX X X X X X",
           "X X             X X X   X",
           "X   XXXX XXXXXX X X X XXX",
           "XXXX   X X        X X XXX",
           "X  X XXX X XXXXXXXX X XXX",
           "X        X X     XX X XXX",
           "X XXXXXXXX X XXX X  X  XX",
           "X        X     X X XXX XX",
           "XXXXXXXX XXXXXXX X XXX XX",
           "XX     X X    XX X X   XX",
           "X        X XX XX X X X XX",
           "X  XXXXXXX XX    X X X XX",
           "X  XXXXXXX XXXXXXX X X XX",
           "X        X X       X X XX",
           "X  XXXXX X X XXXX X  X XX",
           "X      X X     XX X X  XX",
           "XXXXXX X XXXXXXXX X XXXXX",
           "X               X X    EX",
           "XXXXXXXXXXXXXXXXXXXXXXXXX"]

levels = [level_1, level_2, level_3, level_4]


def setup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                wall.goto(screen_x, screen_y)
                wall.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                dog.goto(screen_x, screen_y)
            if character == "E":
                bone.goto(screen_x, screen_y)
                final.append((screen_x, screen_y))


wall = Wall()
dog = Dog()
bone = Bone()
walls = []
final = []
i = 0


def main():
    Window.bgcolor("black")
    global i
    global wall
    global dog
    global bone
    global walls
    global final
    if i != 0:
        if i <= 3:
            Window.title("MAZE GAME (LEVEL " + str(i + 1) + ")")
        else:
            pass
        wall = Wall()
        dog = Dog()
        bone = Bone()
        final = []
        walls = []
    setup(levels[i])
    i = i + 1
    turtle.onkey(dog.go_left, "Left")
    turtle.onkey(dog.go_right, "Right")
    turtle.onkey(dog.go_up, "Up")
    turtle.onkey(dog.go_down, "Down")
    turtle.listen()
    Window.mainloop()


main()
