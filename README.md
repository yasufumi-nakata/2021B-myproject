# 2021B-myproject

このレポジトリは2021年秋学期の情報基礎2の授業内に作成したmyprojectを改良して公開したものです。<br>

## 遊び方

このプロジェクトは開始すると画像が表示されます。**スペースキーを押すこと**で場面が転換し、８回目からはボール拾いのゲームとなります。そこまででゲームは終了です。

## 動作イメージ

https://user-images.githubusercontent.com/52214705/193990285-566ab7a8-7ace-4ba3-a20b-40e546e25375.mov




## このレポジトリについての説明
[myproject](myproject)フォルダの中に全てのコード実行に必要なファイルがあります。　　<br>
[.gitignore](.gitignore)ファイルはgitの更新の際に無視するファイルを指定しています。基本的には無視して大丈夫なものです。<br>
[requirements.txt](requirements.txt)ファイルには必要となるパッケージとそのバージョンが明記してあります。  <br>
[README.md](README.md)ファイルはこの文書を表示させています。<br>

## myprojectフォルダについての説明

[myproject.py](myproject.py)ファイルはこのゲームの基盤となるファイルです。このファイルを実行することでゲームを遊ぶことができます。　<br>
このファイルのコートはAppクラス、Ballクラス、PadクラスとPlayクラスの４つのクラスから成っています。  
### Appクラスについて
Appクラスはこのプログラムの主となるクラスです。各場面転換をupdate関数で、draw関数で開始時のテキストを表示しています。<br>
### Ballクラスについて
このクラスでは最後のボールゲームのボールの挙動を制御しています。<br>
### Padクラスについて
このクラスでは最後のボールゲームのパッドの挙動を制御しています。<br>
### Playクラスについて
このクラスでは最後のボールゲームのゲームの挙動を制御しています。update関数でボールの取得を確認し、draw関数でボールなどの描写をしている。<br>

### 前調査
ボールゲームの際のアイコンにはモチーフがある。<br>
モチーフ元：[INTERACTIVE LIVE SHOW 2022 ZCON SUSUMU HIRASAWA](https://www.susumuhirasawa.online/2022zcon)<br>
また、ストーリーの元ネタは以下。<br>
元ネタ:[加藤寛先生: Take Off Rallyのスピーチ](https://youtu.be/axhCdim2njc)
