# N 個数のグッズがある。
# グッズi の重さは W_i である。
    # 1 <= i <= N
# D 個の福袋にする
    # 各福袋には、一つ以上のグッズが入る。その重さの総和を x_i とする。
# x_1, x_2, ..., x_D の分散の最小値を求める。

# ----------- 解答 ------------
import sys
N, D = map(int, input().split())
W = list(map(int, input().split()))


# print(W)

# 平均値は
# ave(x) = sum(x_i) / D = sum(W) / D である。

x_ave = sum(W) / D

# 分散が最小になるようにしたい。
    # イメージは、どの福袋もできるだけ x_ave に近い重さにしたい。
    # argmin_{x} V
        # = argmin_{x} sum_{i=1}^{D} (x_i - x_ave)^2
        # = argmin_{x} sum_{i=1}^{D} (x_i^2 - 2 x_i x_ave + x_ave^2)
        # = argmin_{x} sum_{i=1}^{D} (x_i^2) - 2 x_ave sum_{i=1}^{D} (x_i) + D x_ave^2
        # = argmin_{x} ave(x^2) - 2 x_ave sum_{i=1}^{D} (x_i) + D x_ave^2
        # = argmin_{x} ave(x^2) - (ave(x))^2
        # = argmin_{x} ave(x^2) - ave(x)^2
        # = argmin_{x} ave(x^2)
        # = argmin_{x} sum(x^2)

# 2 <= D <= N <= 15 であり、割と小さい。効率的に全探索したい。
# 最小にしたいのは、sum(x^2) である。
# 拘束条件は、sum(x_i) = sum(W) である。

# 組み分けの全探索をする。
# W を D 個に分ける。

import itertools
for w_shuffled in itertools.permutations(W):
    # 先頭から y_1, y_2, ..., y_D に分ける。
    # ただし、1 <= y_1 <= y_2 <= ... <= y_D かつ、y_1 + y_2 + ... + y_D = N とする。
    pass

