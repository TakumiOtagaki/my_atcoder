def get_input():
    N, M = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    R = [int(input()) for _ in range(M)]
    return N, M, L, R

def main():
    N, M, L, R = get_input()
    mod = 10 ** 9 + 7
    L.sort()
    R.sort()
    i = 0
    j = 0
    count = 0
    for l in L:
        while j < M and R[j] < l:
            j += 1
        count += M - j
        count %= mod
    print(count)
    return

if __name__ == '__main__':
    main()