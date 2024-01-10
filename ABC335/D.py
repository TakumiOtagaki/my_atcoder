# グリッド：N × N のマス目
# N = 3, 5, 7, ..., 45
# 上から i, 左から j 番目のマス目を (i, j) と表す。

# 条件
    # 竜を配置：1, 2, ..., N^2 - 1 の部品からなる竜。
    # 中央のマス （ (N+1)/2, (N+1)/2 ）にはユーザがいる
    # ユーザがいるマスには部品を載せない（ただ 1 マス）
    # ユーザがいない残りのますには、部品を載せなくてはならない
    # 部品 x と x-1 は、縦横に隣り合うマスに載せなくてはならない。
        # ななめは禁止する

# point: 
    # https://zoshigayan.net/i-had-misunderstood-slice/
    # k 個のスライスは O(k) かかる。
# 入力
    # N

# 出力
# 行列 X_ij: ユーザは T で部品はその部品の番号で表す


# ------------------- 解答 --------------------

N = int(input())

# 真ん中から渦巻き状に配置すればよい。上から始めて、右、下、左、上、右、下、左、... と繰り返す。
# 辺の長さを s すると、s = 1, 2, 3, ..., N-1 となる。

# 座標のリスト
d = [ [0 for _ in range(N)] for __ in range(N) ]

# 1. 真ん中のマスにユーザを配置する
# x, y = (N+1)//2 , (N+1)//2 
x, y = N//2, N//2
d[x][y] = 'T'

# 2. 1 つ目の部品を配置する
id = 0
s, rot = 1, "up"

while id < N**2 and x >= 0 and y >= 0:
    # rot = right: 右に進む

    if rot == "up":
        for i in range(s):
            if id == N**2:
                break
            x -= 1
            if x < 0:
                break
            id += 1
            d[x][y] = id
        rot = "right"
    # rot = right: 下に進む
    elif rot == "right":
        for i in range(s):
            if id == N**2:
                break
            y += 1
            id += 1
            d[x][y] = id
        rot = "down"
        s += 1
    # rot = right: 左に進む
    elif rot == "down":
        for i in range(s):
            if id == N**2:
                break
            x += 1
            id += 1
            d[x][y] = id
        rot = "left"
    # rot = right: 上に進む
    elif rot == "left":
        for i in range(s):
            if id == N**2:
                break
            y -= 1
            id += 1
            d[x][y] = id
        rot = "up"
        s += 1


# 出力
for i in range(N):
    print(*d[i])

