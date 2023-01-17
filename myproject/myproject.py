# coding=utf-8
import pyxel
import random
import math


class App():
    # 全体ゲームの範囲
    # スタート画面と終了画面を表示する
    count = 0

    def __init__(self):
        pyxel.init(400, 400)
        pyxel.blt(20, 20, 0, 0, 0, 190, 190)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.count += 1
        if self.count == 0:
            pyxel.load("script1.pyxres")
            pyxel.blt(100, 150, 0, 0, 0, 255, 218)
        elif self.count == 1:
            pyxel.load("script1.pyxres")
            pyxel.blt(100, 150, 1, 0, 0, 255, 218)
        elif self.count == 2:
            pyxel.load("script1.pyxres")
            pyxel.blt(100, 150, 2, 0, 0, 255, 218)
        elif self.count == 3:
            pyxel.load("script2.pyxres")
            pyxel.blt(100, 150, 0, 0, 0, 255, 218)
        elif self.count == 4:
            pyxel.load("script2.pyxres")
            pyxel.blt(100, 150, 1, 0, 0, 255, 218)
        elif self.count == 5:
            pyxel.load("script2.pyxres")
            pyxel.blt(100, 150, 2, 0, 0, 255, 218)
        elif self.count == 6:
            pyxel.load("script3.pyxres")
            pyxel.blt(100, 150, 0, 0, 0, 255, 218)
        elif self.count == 7:
            pyxel.load("script3.pyxres")
            pyxel.blt(100, 150, 1, 0, 0, 255, 218)
        elif self.count == 8:
            Play()
            print("####")
        #     pyxel.load("script3.pyxres")
        #     pyxel.blt(100, 150, 2, 0, 0, 255, 218)
        # if App.sscore == 2:
        #    print("Play.score")
        # print(sscore)

        # 進行用
    def draw(self):
        # print("b")
        # pyxel.blt(20, 20, 0, 0, 0, 190, 190)
        pyxel.text(10, 10, 'Press SPACEBAR to START', 12)
        # pyxel.init(400, 400)
        # pyxel.load("my_resource.pyxres")

        # class Novel:
        #     def __init__(self):
        #         pass

        #     def update(self):
        #     def characters(self):


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
