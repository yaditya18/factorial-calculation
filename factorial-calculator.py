n = int(input("enter the number to find the factorial of\n"))
ans = 1
for i in range(1, n + 1):
    ans = ans * i
print(ans)
