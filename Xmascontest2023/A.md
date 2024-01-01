# 2023 XmasContest A
https://atcoder.jp/contests/xmascon23/editorial/8972

## 問題の解釈
### 我々ができること
まず、$k$ を 2, 3, 4 から一つ選んで、

```math
\begin{align}
a = 2^{\dfrac{1}{k}}
\end{align}
```
のもとで、
$1 : 1+a$ の長方形を利用することができる。

### ゴール
$1:a$ の長方形タイルを重ならないように、いっぺんの長さ $r \in R$ の正方形に余白がないように敷き詰める。
そのようなタイルの敷き詰め方を
