# N マス
# M 個数のマスに石がある
# X_i に A_i 個数ある。A_i >= 0

# 操作P: マス i に石がある時、i から石を一つi+1に移動させる

# N 個数のマス全てに石がちょうど一つずつ入っている状態にするために必要な回数の最小値。
from sys import exit
N, M = map(int, input().split())
X = map(int, input().split())
A = map(int, input().split())

# X, A で X についてソートする。昇順
X, A = zip(*sorted(zip(X, A)))
# print(f"X: {X}, A: {A}")

total_stones = sum(A)
if total_stones != N:
    print(-1)
    exit()

# 貪欲法でいい。左側から完成させていく。
target_pos = 1
total_operations = 0

for x, a in zip(X, A):
    if target_pos < x:
        # ターゲット位置をxに更新
        target_pos = x
    # 必要なターゲット位置がNを超えるか確認
    if target_pos + a - 1 > N:
        print(-1)
        exit()
    # 操作回数の計算
    # 各石をtarget_posから順に割り当てる
    # 操作回数は (target_pos - x) + (target_pos +1 - x) + ... + (target_pos + a -1 -x)
    # これは a*(target_pos - x) + (a*(a-1))//2
    operations = a * (target_pos - x) + (a * (a - 1)) // 2
    total_operations += operations
    # 次のターゲット位置を更新
    target_pos += a

# 最終的にターゲット位置がN+1であることを確認
if target_pos - 1 != N:
    print(-1)
else:
    print(total_operations)



    

