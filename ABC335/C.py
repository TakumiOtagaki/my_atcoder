# 1, 2, ..., N の部品がある
# 部品1: 頭

# 初期化
    # 部品 i: (i, 0) に位置する

# 操作（Query）
    # 1 C: 頭を方向 C に 1 移動させる
        # C = R, L, U, D
        # 頭以外の全ての部品は頭に追従する。
        # つまり部品 i は移動前に部品 i-1 があった場所に移動する。
    # 2 p: p のある座標を求める

# point:
    # 先頭を pop したいような時は、逆順にしてしまう。さらに先にメモリを確保しておけば、インデックス指定で配列に代入していける。

# 入力
# N, Q
# q_1
# q_2
# ...
# q_Q

# -------------------------------------------------------------
# input の取得

N, Q = map(int, input().split())

# 逆順の A
    # 頭が最後尾にある状態
A = [(0, 0) for _ in range(N+Q)] # できる限り大きい量を確保しておく。
for i in range(1, N+1):
    A[i-1] = (N - i + 1, 0)
# 後ろの方は全て余っている。


x, y = 1, 0 # head の座標
head_pointer = N
for _ in range(Q):
    
    T, C = input().split()
    if T == "1":
        if C == "R":
            x += 1
        elif C == "L":
            x -= 1
        elif C == "U":
            y += 1
        elif C == "D":
            y -= 1
        else:
            raise ValueError
        A[head_pointer] = (x, y)
        head_pointer += 1
        # print("A = ", A)
        
    elif T == "2":
        p = int(C)
        # p は 1-indexed
        # p が指す座標を求める
        # A は 0-indexed

        # head_pointer から遡る
        
        a, b = A[head_pointer - p]
        print(a, b)

        
# -------------------------------------------------------------

