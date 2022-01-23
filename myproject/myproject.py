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
        pyxel.text(200, 200, 'Press SPACEBAR to START', 12)
        pyxel.text(200, 250, 'welcome to the story', 12)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.count == 0:
            pyxel.load("script1.pyxres")
            pyxel.blt(200, 250, 0, 0, 0, 164, 117)
        elif self.count == 1:
            pyxel.load("script1.pyxres")
            pyxel.blt(200, 250, 1, 0, 0, 242, 145)
        elif self.count == 2:
            pyxel.load("script1.pyxres")
            pyxel.blt(200, 250, 2, 0, 0, 220, 156)
        elif self.count == 3:
            pyxel.load("script2.pyxres")
            pyxel.blt(200, 250, 0, 0, 0, 255, 136)
        elif self.count == 4:
            pyxel.load("script2.pyxres")
            pyxel.blt(200, 250, 1, 0, 0, 255, 136)
        elif self.count == 5:
            pyxel.load("script2.pyxres")
            pyxel.blt(200, 250, 2, 0, 0, 234, 120)
        elif self.count == 6:
            pyxel.load("script3.pyxres")
            pyxel.blt(200, 250, 0, 0, 0, 224, 127)
        elif self.count == 7:
            pyxel.load("script3.pyxres")
            pyxel.blt(200, 250, 1, 0, 0, 255, 218)
        elif self.count == 8:
            pyxel.load("script3.pyxres")
            pyxel.blt(200, 250, 2, 0, 0, 252, 208)

        # 進行用

    def draw(self):
        pyxel.blt(20, 20, 0, 0, 0, 190, 190)
        pyxel.text(200, 200, 'Press SPACEBAR to START', 12)
        pyxel.init(400, 400)
        pyxel.load("my_resource.pyxres")


# class Novel:
#     def __init__(self):
#         pass

#     def update(self):

#     def characters(self):


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
