# H × W のグリッド A と B がある
# 1 <= i <= H, 1 <= j <= W の各 i, j について、A[i][j] と B[i][j] は整数が入っている。

# 以下の二つのうちいずれか一つの操作を 0 回以上 好きなだけ行うことができる。
    # 1. 1 <= i <= H−1 を満たす整数 i を選んで A の i 行目と i+1 行目を入れ替える。
    # 2. 1 <= j <= W−1 を満たす整数 j を選んで A の j 列目と j+1 列目を入れ替える。

# この操作を行って A = B となるかどうか判定せよ。
    # 一致可能な場合は、その最小回数を求めよ。
    # 一致不可能な場合は、-1 を出力せよ。

# 例：
"""
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
1 3 2 5 4
11 13 12 15 14
6 8 7 10 9
16 18 17 20 19
"""

# get input
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

def check(A, B):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True

# print(A, B)
# 異なる要素が入っていたらアウトなので、flatten してから一致性をみる
A_list = [A[i][j] for i in range(H) for j in range(W)]
B_list = [B[i][j] for i in range(H) for j in range(W)]
if sorted(A_list) != sorted(B_list):
    print(-1)
    exit()

# print("hello")

# 転倒数の計算
def inversion_number(array):
    n = len(array)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                count += 1
    return count


# H, W <= 5 という状況であり、かなり小さいので、全探索できる
# 行の swap の場合の数は、H! 通り、列の swap の場合の数は、W! 通り
    # 初めの行のインデックスを P = [0, 1, 2, ..., H-1] とすると、P を swap によって並べ替えるものが、操作後の状態を表す。
        # 最小回数を知りたいので、P を辞書順に並べ替えるのが最小回数の操作となる。
    # Q = [0, 1, 2, ..., W-1] についても同様。
# つまり、H! * W! 通りの全探索でよい
    


import itertools
P = [i for i in range(H)]
Q = [i for i in range(W)]
ans = 0
for p in itertools.permutations(P):
    for q in itertools.permutations(Q):
        # print(p, q)
        # print(A)
        # print(B)
        # print()
        # print()
        A_ = [ [A[i][j] for j in q] for i in p]
        if check(A_, B):
            flag = True
            # A, B の転倒数を計算
            a, b = inversion_number(p), inversion_number(q)
            print(min(a + b, ans))
            exit()

        ans += 1

print(-1)


