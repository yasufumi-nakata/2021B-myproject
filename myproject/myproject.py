# coding=utf-8
import pyxel
import random
import math


class App():
    def __init__(self):
        pyxel.init(400, 400)
        pyxel.blt(20, 20, 0, 0, 0, 190, 190)
        self.count = 0
        self.script = ["script1.pyxres", "script2.pyxres", "script3.pyxres"]
        self.script_index = 0
        self.script_frame = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.count += 1
            if self.count == 9:
                Play()
                print("####")
            elif self.count > 2:
                self.script_index = (self.count-1) // 3
                self.script_frame = (self.count-1) % 3
                pyxel.load(self.script[self.script_index])
                pyxel.blt(100, 150, self.script_frame, 0, 0, 255, 218)
        elif self.count == 0:
            pyxel.text(10, 10, 'Press SPACEBAR to START', 12)

    def draw(self):
        pass


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


'''
乱数を使用　2点
リストを使用　3点
複数個のクラス定義を使用　2点
self以外の引数を持つメソッドを使用　3点
キー入力を使用　2点
マウス座標を使用　2点
授業で出てこなかった機能を使用　5点
異なる規則によって動く図形が3種類以上ある　3点
アルゴリズムの複雑さ（無駄に複雑な部分は評価に含めない）　10点
ゲームとしての面白さ（ゲーム以外の場合は、その分野における評価）　4点
独創性　4点
'''

'''

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
script1
世界は闇に
包まれた時代から
世界が照らされた
時代になりました。

しかし、その光は歪んだ物
となっていった。
歪んだ光からは
歪んだものしか生まれない。

そのため世界は
それぞれの色で照らされ、
同じものも違う物として
扱われるようになった。
script2
そこで我々は正しい光を
見せることを計画する。
世界に散らばった
フクロウを集め、
一度無に返す。

そして正しい光を放つ
フクロウを育てるのである。
世界に飛び立った先代たちは
確かに闇を照らした。

しかしやがて時間が経ち
他のものたちと同じように
フクロウも闇の先を
見通せなくなっていった。
script3
そのため次のフクロウが
必要となるのである。
今、新たなフクロウが
羽ばたこうとしていた。

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

これから臍帯の裁断者たる
あなたたちにはフクロウたちの
産婆として彼らに
能力を与えてもらいます。
これから示される選択肢
から皆さんが与えたいもの
を選んでください。


論理　感情　思い
自己　戦略　戦術
情欲　絶望　苦悶

ありがとう。
フクロウは産み落とされた。
彼らがどのような物語を
生み出すのかを
楽しみにしてくれ。
これはささやかな選別だ。
受け取ってほしい。

'''


App()
