# N 本の bit, S
# S[i] == X: 虫歯
# S[i] == O: 歯
# 連続する K 本数が O で大丈夫な時、イチゴを一つ食べられる(c+=1).
# 何個食べられるか

N, K = map(int, input().split())
S = input()


def solve(N, K, S):
    c = 0
    for i in range(N):
        if S[i:i+K].count("O") == K:
            c += 1
            S[i:i+K] = "X" * K

    return c

print(solve(N, K, list(S)))