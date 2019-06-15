def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=fibonacci(n-1)+fibonacci(n-2)
        print(a)
        return a
num = int(input("enter number"))
print(fibonacci(num))