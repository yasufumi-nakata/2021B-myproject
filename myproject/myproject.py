# coding=utf-8
import pyxel
import random
import math


class App:
    # ゲーム全体の状態を管理するクラス
    count = 0

    def __init__(self):
        pyxel.init(400, 400)
        pyxel.blt(20, 20, 0, 0, 0, 190, 190)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.count += 1

        if self.count == 8:
            Play()
            print("####")

        if self.count < 8:
            script_name = f"script{self.count // 3 + 1}.pyxres"
            pyxel.load(script_name)
            pyxel.blt(100, 150, self.count % 3, 0, 0, 255, 218)

    def draw(self):
        pyxel.text(10, 10, 'Press SPACEBAR to START', 12)


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
        if (self.x <= 0) or (self.x >= 400):
            self.vx *= -1
        if self.y >= 400:
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
        if (thisball.y >= 395) and (thisball.x >= self.x-20) and (thisball.x <= self.x+20):
            thisball.restart()
            return True
        else:
            return False


class Play:
    score = 0

    def __init__(self):
        self.miss = 0
        self.gameover = False
        self.balls = [Ball(), Ball(), Ball()]

        pyxel.load("beacon.pyxres")
        self.p = Pad()
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
                Play.score += 1
                if self.score % 1 == 0:
                    Ball.speed = 3
                    self.balls.append(Ball())
        self.p.x = pyxel.mouse_x

    def draw(self):
        pyxel.cls(7)
        for b in self.balls:
            pyxel.circ(b.x, b.y, b.ballcolor, b.ballsize)
        pyxel.rect(self.p.x-20, 395, 40, 5, 14)

        pyxel.text(10, 10, "score : " + str(Play.score), 0)
        pyxel.blt(20, 20, 0, 0, 0, 35, 35)


App()
