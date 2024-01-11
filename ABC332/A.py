N, S, K = map(int, input().split())

total = 0

for i in range(N):
    p_i, q_i = map(int, input().split())
    total += p_i * q_i

if total >= S:
    pass
else:
    total += K

print(total)