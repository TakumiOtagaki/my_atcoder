#  0 <= N <= 21
# 0 <= x + y + z <= N となる (x, y, z) の組み合わせを辞書順に列挙する
# x + y + z <= N である点に注意（等号ではない）
N = int(input())

ans = []
for x in range(N+1):
    for y in range(N-x+1):
        # z = N - x - y
        # x + y + z <= N となる (x, y, z) の組み合わせを辞書順に列挙する
        for z in range(N-x-y+1):
            if x + y + z <= N:
                ans.append((x, y, z))
            else:
                break
            


# 半角スペース区切り
for x, y, z in ans:
    print(f"{x} {y} {z}" )