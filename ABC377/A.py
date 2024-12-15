# S = input()
# if set(list(S)) == set(list("ABC")):
#     print("Yes")
# else:
#     print("No")

a = "Yes" if set(list(input())) == set(list("ABC")) else "No"
print(a)