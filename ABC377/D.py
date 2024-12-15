# 長さ N の自然数列 L, R
# 整数 M 

# S = {(l, r) | 1 <= l <= r <= M, for all i (1 <= i <= N, [l, r] not includes [L_i, R_i] completely)}

# 1 <= N, M <= 2 * 10^5
# 1 <= L_i <= R_i <= M
# import time

def get_input():
    N, M = map(int, input().split())
    L = [0 for _ in range(N)]
    R = [0 for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())

    return N, M, L, R

def set_include(l, r, Li, Ri):
    # True if [l, r] includes [Li, Ri] completely else False
    return (l <= Li) and (Ri <= r)

# 探すのは
# #(l', r') = {(l', r') | for \exists i (1 <= i <= N, [l', r'] includes [L_i, R_i])}
# とすると #(l, r) = #U - #(l', r') となる

# def count_l_r(N, M, L, R):
#     count = 0
#     for l in range(1, M + 1):
#         for r in range(l, M + 1):
#             for i in range(N):
#                 if set_include(l, r, L[i], R[i]): break
#             else:
#                 count += 1

#     return count

def binary_search_left(L, l):
    # L は昇順に並んでいる。l < L[i] となる最小の i を返す
    left = 0
    right = len(L)
    while right - left > 1:
        mid = (left + right) // 2
        if L[mid] <= l:
            left = mid
        else:
            right = mid
    return left

# def test_binary_search_left():
#     array = [1, 2, 3, 4, 5]
#     assert binary_search_left(array, 0) == 0
#     assert binary_search_left(array, 1) == 0
#     assert binary_search_left(array, 2) == 1
#     assert binary_search_left(array, 3) == 2
#     assert binary_search_left(array, 4) == 3
#     assert binary_search_left(array, 5) == 4

# test_binary_search_left()



def count_intervals(N, M, L, R):
    # 全ての区間をL_iの昇順にソート
    sorted_intervals = sorted(zip(L, R), key=lambda x: x[0], reverse=False)
    sorted_L = [x[0] for x in sorted_intervals]
    sorted_R = [x[1] for x in sorted_intervals]
    
    count = 0
    for l in range(1, M+1):
        # [l, r] includes [ L_i, R_i ] completely を考えるので、 l < L_i となるはじめの i を知れればいい
        i = binary_search_left(sorted_L, l)
        if i == N:
            count += M - l + 1
            continue

        R_candidates = sorted_R[i:]
        rmin = min(R_candidates)
        count += rmin - l

    return count



def main():
    N, M, L, R = get_input()
    # print(N, M, L, R)
    # print(count_l_r(N, M, L, R))

    print(count_intervals(N, M, L, R))



if __name__ == '__main__':
    # start = time.time()
    main()
    # print(time.time() - start)