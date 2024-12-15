# 長さ 8 の文字列 Si が 8個得られる
S = [input() for _ in range(8)]

# Sij == "." ならば empty
# Sij == "#" ならば ルーク


# 空間に存在するルークたちに取られない範囲が何個あるか数えるだけ。
# ルークの存在する (i, j) をタプルで保存
rooks = []
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            rooks.append((i, j))

# 8x8 の盤面を作る
import numpy as np
board = np.zeros((8, 8), dtype=int)



# ルークがアクセスできるところを 1 にする
for rook in rooks:
    i, j = rook
    board[i, :] += 1
    board[:, j] += 1

count = board[board == 0].shape[0]

print(count)


