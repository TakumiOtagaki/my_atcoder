# マグカップに水を入れたり、水を捨てたりして、水の量を変化させる。

K, G, M = map(int, input().split())

glass, mug = 0, 0
for _ in range(K):
    if glass == G:
        glass = 0
    elif mug == 0:
        mug = M
    else:
        # マグカップが空になるかグラスがいっぱいになるまで水を移す。
        # このとき、マグカップの水の量がグラスの水の量を超えないようにする。
        if mug <= G - glass:
            glass += mug
            mug = 0
        else:
            mug -= (G - glass)
            glass = G



print(glass, mug)