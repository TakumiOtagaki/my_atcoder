# 競プロなので時間も測定しておく
# import time

# from numba import jit


# N^2 マスに M 個存在しているナイトに取られないマスの数を数える
moves = [
        (1, 2),
        (2, 1),
        (-1, 2),
        (-2, 1),
        (1, -2),
        (2, -1),
        (-1, -2),
        (-2, -1)
    ]

def get_input():
    N, M = map(int, input().split())
    knights = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, knights

# @jit
def can_move(x, y, dx, dy, N):
    return 1 <= x + dx <= N and 1 <= y + dy <= N

def knight_movables(x, y, N):
    return [(x + dx, y + dy) for dx, dy in moves if can_move(x, y, dx, dy, N)]

def main():
    N, M, knights = get_input()
    all_cells = N * N

    attacked_cells = set()
    for knight in knights:
        x, y = knight
        attacked_cells.add(knight)
        for move in knight_movables(x, y, N):
            attacked_cells.add(move)


    count = all_cells - len(attacked_cells)
    print(count)
    return

if __name__ == '__main__':
    # start = time.time()
    main()
    # print(time.time() - start)