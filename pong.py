import sys, keyboard, time, random
sys.stdout.write("\033[2J")

screeny, screenx = 40, 80
screen = [["0" for i in range(screenx)] for i in range(screeny)]

class Player:
    def __init__(self, y):
        self.y = y
        self.score = 0
    
    def go_up(self):
        if self.y[0] > 0:
            for i in range(3):
                self.y[i] -= 1
    def go_down(self):
        if self.y[2] < screeny-1:
            for i in range(3):
                self.y[i] += 1

class Ball:
    def __init__(self):
        self.y = screeny/2
        self.x = screenx/2
        self.direction = 1
        self.flap = False

    def go(self):
        if self.y == 0:
            self.y += 1
            if self.direction == 1:
                self.direction = 3
            elif self.direction == 7:
                self.direction = 5
        elif self.y == screeny-1:
            self.y -= 1
            if self.direction == 3:
                self.direction = 1
            elif self.direction == 5:
                self.direction = 7
        elif self.x == 0:
            player_two.score += 1
            self.y = screeny/2
            self.x = screenx/2
            self.direction = random.choice([1, 3, 5, 7])
        elif self.x == screenx-1:
            player_one.score += 1
            self.y = screeny/2
            self.x = screenx/2
            self.direction = random.choice([1, 3, 5, 7])
        elif self.x == 3 and self.y in player_one.y:
            self.x += 1
            if self.direction == 1:
                self.direction = 7
            elif self.direction == 3:
                self.direction = 5
        elif self.x == (screenx-4) and self.y in player_two.y:
            self.x -= 1
            if self.direction == 5:
                self.direction = 3
            elif self.direction == 7:
                self.direction = 1
        else:
            self.flap = not self.flap
            if self.direction == 1:
                if self.flap:
                    self.x -= 1
                else:
                    self.y -= 1
            elif self.direction == 3:  
                if self.flap:
                    self.x -= 1
                else:
                    self.y += 1
            elif self.direction == 5:
                if self.flap:
                    self.x += 1
                else:
                    self.y += 1
            elif self.direction == 7:
                if self.flap:
                    self.x += 1
                else:
                    self.y -= 1
    

player_one = Player([18, 19, 20])
player_two = Player([18, 19, 20])
ball = Ball()

while True:
    ball.go()

    if keyboard.is_pressed("w"):
        player_one.go_up()
    if keyboard.is_pressed("s"):
        player_one.go_down()
    
    if keyboard.is_pressed("up"):
        player_two.go_up()
    if keyboard.is_pressed("down"):
        player_two.go_down()

    for i in range(screeny):
        for j in range(screenx):
            if i == ball.y and j == ball.x:
                screen[i][j] = "7"
            else:
                screen[i][j] = "0"
            if i in player_one.y:
                screen[i][2] = "7"
            if i in player_two.y:
                screen[i][screenx-3] = "7"

    sys.stdout.write("\033[H")
    print(f"\t\033[1mPlayer 1: {player_one.score}\tPlayer 2: {player_two.score}\033[m")
    for i in screen:
        for count, j in enumerate(i):
            print(f"\033[4{j}m  \033[m", end="\n" if count == screenx-1 else "")
    
    time.sleep(0.02)