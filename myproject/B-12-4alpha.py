import pyxel
import math
import random


class Ball:
    speed = 3

    def restart(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
        self.ballcolor = (random.randint(0, 15))
        self.ballsize = (random.randint(0, 15))

    def move(self):
        if (self.x <= 0) or (self.x >= 200):
            self.vx *= -1
        if self.y >= 200:
            # self.restart()
            self.vy *= -1
        if self.y <= 0:
            self.vy *= -1
            return True
        else:
            return False

    def __init__(self):
        self.restart()


class Pad:
    def __init__(self):
        self.x = 100

    def catch(self, thisball):
        if (thisball.y >= 195) and (thisball.x >= self.x-20) and (thisball.x <= self.x+20):
            thisball.restart()
            return True
        else:
            return False


class App:
    def __init__(self):
        self.score = 0

        self.miss = 0
        self.gameover = False
        self.balls = [Ball(), Ball(), Ball()]

        pyxel.init(200, 200)

        # pyxel.sound(0).set(note='C0', tone='T', volume='7', effect='N', speed=30)
        # pyxel.sound(1).set(note='B3G3', tone='P', volume='3', effect='N', speed=10)
        self.p = Pad()
        # pyxel.load("beacon.pyxres")
        # pyxel.blt(20, 10, 0, 0, 0, 35, 35,)
        # self.balls.append(Ball())
        pyxel.run(self.update, self.draw)

    def update(self):
        for b in self.balls:
            b.x += (b.vx * Ball.speed)
            b.y += (b.vy * Ball.speed)
            if b.move() == True:
                pyxel.play(0, 0)
            if self.p.catch(b) == True:
                pyxel.play(0, 1)
                Ball.speed += 0.1
                self.score += 1
                if self.score % 10 == 0:
                    Ball.speed = 3
                    self.balls.append(Ball())
        self.p.x = pyxel.mouse_x

    def draw(self):

        pyxel.cls(7)
        for b in self.balls:
            pyxel.circ(b.x, b.y, b.ballcolor, b.ballsize)
        pyxel.rect(self.p.x-20, 195, 40, 5, 14)

        pyxel.text(10, 10, "score : " + str(self.score), 0)


App()
