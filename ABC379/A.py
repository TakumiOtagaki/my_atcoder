# N = ３桁の数
# N = 100 a + 10 b + c
# print(bca cab)

a,b,c = tuple(list(input()))

bca = b + c + a
cab = c + a + b

print(f"{bca} {cab}")
