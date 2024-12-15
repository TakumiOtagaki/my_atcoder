# 10**100 の植木鉢
# Q 個数のクエリ
# 1: 空の植木鉢を一つ選んで植える。その時の植物の高さは 0
# 2 T: 植えてある植物の高さが T 増加する
# 3 H: 高さが H 以上の食鬱を全て収穫し、収穫した植物の数を出力する
# 1 <= Q <= 2 * 10^5
# 1 <= T, H <= 10^9
# 3 H が少なくとも一度は出現


import numpy as np
Q = int(input())


def parse_query():
    query = input().split()
    if len(query) == 1:
        return (int(query[0]),)
    else:
        return (int(query[0]), int(query[1]))

def solve(Q):
    MAX_SIZE = int(2 * 10**5) + 4
    plants = np.zeros(MAX_SIZE, dtype=int) - 1
    for i in range(Q):
        query = parse_query()
        if query[0] == 1:
            plants[i] = 0
        elif query[0] == 2:
            T = query[1]
            plants = np.where(plants >= 0, plants + T, plants)
        elif query[0] == 3:
            H = query[1]
            can_harvest = np.where(plants >= H)
            harvested = len(can_harvest[0])
            plants[can_harvest] = -1
            print(harvested)

solve(Q)