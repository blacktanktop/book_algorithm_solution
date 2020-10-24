# book_algorithm_solutionの概要
[問題解決力を鍛える!アルゴリズムとデータ構造](https://www.amazon.co.jp/dp/4065128447)の章末問題の実装

---
## 内容
* 各章の章末問題のPython実装(solutionsディレクトリ以下)
* solutions/python/以下に章ごとにPython実装を配置
* Julia実装もしたい(未定)
* 出力はただ単に最終的な解を出すのではなくて、理解が深まるように適宜print文を入れることもある。

## 実行
### 実行環境
* MacBook Pro (13-inch, Late 2016)
* Python3.8.2で動くことを確認
  * 多分Python3.5以降なら同じように動くとは思う
  * 複雑な計算を解く場合などのケースの時に[SymPy](https://github.com/sympy/sympy)(1.6.2)を使うこともある(例：4.3) 。
  以下のようにしてインストールを行う。
  ```
  pip install sympy
  ```
### 実行例
基本的に、コードを実行して、入力待ちになるのでそのまま値を入力するか、実行時に入力用のテキストを用意してリダイレクトする
#### 自分の好きに入力値を入れたい場合（Enterすると入力待ちになる）
```
python solution_3_1.py
# Enterとすると入力待ちになるので適した形でを入力する
10 7
3 5 8 9 7 10 22 1 2 100
# 出力
4
```
```
python solution_4_1.py
# Enterとすると文章が出てきて、入力待ちになるので適した形でを入力する
0以上の整数を標準入力するとTribonacciを出力する
10
# 出力
Tribonacci list [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
再帰によるTribonacci sequenceの第10項の計算の値：81
```

#### リダイレクトする場合
```
python solution_3_1.py < solution_3_1.txt
```

## 簡単な解説
[自分のブログ（くろたんく雑記帳）](https://blacktanktop.hatenablog.com/)に以下を書く。
* [全体大枠記事](https://blacktanktop.hatenablog.com/entry/2020/10/16/133402)
* 各章の詳細記事
  * [【第３章】設計技法(1)：全探索](https://blacktanktop.hatenablog.com/entry/2020/10/16/133149)
  * [【第４章】 設計技法(2)：再帰と分割統治法](https://blacktanktop.hatenablog.com/entry/2020/10/18/203456)
  * [【第５章】 設計技法(3)：動的計画法](https://blacktanktop.hatenablog.com/entry/2020/10/20/075549)
  * [【第６章】 設計技法(4)：二分探索法](https://blacktanktop.hatenablog.com/entry/2020/10/21/100500)
  * [【第７章】 設計技法(5)：貪欲法](https://blacktanktop.hatenablog.com/entry/2020/10/24/144929)

## 書籍のレポジトリ
[drken1215/book_algorithm_solution](https://github.com/drken1215/book_algorithm_solution)  
主にC++での実装が書かれている。
