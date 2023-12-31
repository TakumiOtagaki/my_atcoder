# 2023 XmasContest A
https://atcoder.jp/contests/xmascon23/editorial/8972

## 問題の解釈
### 我々ができること
まず、$`k`$ を $`2, 3, 4 `$ から一つ選んで、

```math
\begin{align}
a = 2^{\dfrac{1}{k}}
\end{align}
```
のもとで、
$`1 : 1+a`$ の長方形を利用することができる。

### ゴール
$`1:a`$ の長方形タイルを重ならないように、一辺の長さ $r \in R$ の正方形に余白がないように敷き詰めることが目標である。
ただし、$`k \in \lbrace 2, 3, 4 \rbrace`$  をはじめに一つだけ選択し、$r$ についても都合が良いように自分で設定して良い。
また、使うタイルの枚数についても、自分で設定して良い。その枚数を $`n`$ とする。

出力するのは、$`n, k, r`$ と各長方形の座標（$`a_i, b_i, c_i, d_i`$）である。

## 解法
イメージとしては、辺の比が有理数となるような長方形タイルを構築することができれば、それをある整数個だけ並べれば正方形を構築できそう、という考え。
なので、$`1:a`$の長方形タイルを並べることでなんとか $`1 : q`$ （$`q`$ は有理数）の比を作るのが当面の目標になる。

### 定義
「$`1:x`$ の長方形タイルが利用可能である」とは、
「任意の正の実数 $`t`$ に対して、縦と横の長さがそれぞれ $`t, xt`$ or $`xt, t`$ となる」長方形タイルを敷き詰めに利用して良い」という状況を表す。

### アイデア
1. 和
$`1:x`$ と $`1:y`$ の長方形タイルが利用可能だとする。
すると、縦横の長さがそれぞれ$`t, xt`$ と $`y, yt`$ の二つの長方形を横に連結することで、
$`1: (x+y)`$ の長方形タイルを作ることができる。

3. 逆数
$`1:x`$ の長方形タイルが利用可能だとする。すると直ちに
$`\dfrac{1}{x}:1`$ の長方形タイルも利用可能である。

### 具体的なアイデア
$`1: 1+a`$ （ただし、$`a = 1 + 2^{\dfrac{1}{k}}`$） に逆数や和の演算を駆使して、辺比が有理数になるような長方形タイルを作る。

まず逆数を試してみる。
```math
\begin{align}
1: 1+a = \dfrac{1}{1+a} : 1
\end{align}
```
で、ここから計算を進めることができるのは、 $`a = 2^{\dfrac{1}{k}}`$ の元では $`k`$ が奇数でないと話が進まない！従って $k=3$ に限って進めてみる。
すると、$`a^3 = 2`$ である。これを利用する。

```math
\begin{align}
1: 1+a
& =  \dfrac{1}{1+a} : 1 \\
& = \dfrac{(1-a+a^2)}{(1+a)(1-a+a^2)} : 1 \\
& = \dfrac{1 - a + a^2}{1 + a^3} : 1 \\
& = \dfrac{1}{3} (1 - a + a^2) : 1 
\end{align}
```
となり、$`\dfrac{1}{3} (1 - a + a^2) : 1`$ の辺比の長方形は「逆数」の操作によって作成できることがわかった。

続いて、$`1 + a : 1`$ の長方形ができることははじめの問題文の前提から、和をとることによって、

```math
\begin{align}
\dfrac{1}{3} (1 - a + a^2) + (1 + a) : 1 & =
\dfrac{1}{3} (4 + 2a + a^2) : 1
\end{align}
```

となって、$`\dfrac{1}{3} (4 + 2a + a^2) : 1`$ の長方形は、「和」の操作によって作成できることがわかった。

さらに引き続き、逆数をとってみる。（狙いとしては、$` a^3 = 2 `$ だから、$`4`$ や $`2`$ といった係数についてもうまく扱えるかも、という期待がある。）

すると、逆数の操作によって、

```math
\begin{align}
\dfrac{1}{\dfrac{1}{3} (4 + 2a + a^2)} : 1
& = \dfrac{3}{(4 + 2a + a^2)} : 1 \\
& = \dfrac{3}{a^6 + a^4 + a^2} : 1 \\
& = \dfrac{3}{a^2 (1 + a^2 + a^4)} : 1 \\
& = \dfrac{3 (1 - a^2)}{a^2 (1 + a^2 + a^4)(1 - a^2)} : 1 \\
& = \dfrac{3 (1 - a^2)}{a^2 (1 - a^6)} : 1 \\
& = \dfrac{3 (1 - a^2)}{a^2 (1 - 4)} : 1 \\
& = \dfrac{3 a(1 - a^2)}{a^3 (1 - 4)} : 1 \\
& = \dfrac{3 (a - a^3)}{2 (1 - 4)} : 1 \\
& = \dfrac{3 (a - 2)}{2 (-3)} : 1 \\
& = \dfrac{3(2 - a)}{6} : 1 \\
& = \dfrac{(2 - a)}{2} : 1
\end{align}
```

となって、$`\dfrac{(2 - a)}{2} : 1`$ の長方形を作ることができた。
すると $`2-a : 2`$ の長方形を作ることができる。これと、はじめに与えられた $`1+a : 1`$ を縦に並べた $`1+a : 2`$ の長方形を並べることによって（
$`\{(2-a)t, 2t\}, \{(1+a)t, 2t\}`$
）、
$`2 - a + 1 + a : 2`$ つまり $`3:2`$ の長方形を作ることができた。これは辺比が有理数であり、ここからは適当に並べることができるはず。

ここまでをまとめてみると、
1.  $`1+a:1`$ is given
2.  1.の縦と横を入れ替えれば $`\dfrac{1}{3} (1 - a + a^2) : 1 `$ を直ちに得る
3.  1.と2.を並べることで $`\dfrac{1}{3} (4 + 2a + a^2) : 1`$ を得る
4.  3.の縦と横を入れ替えれば $`\dfrac{(2 - a)}{2} : 1`$ を直ちに得る
5.  1.をふたつと 4.を一つ並べることで $`3:2`$ の長方形を得る



```mermaid
graph LR;
1 --> 2 --> 3 --> 4 --> 5
1-->3
1-->5


```
