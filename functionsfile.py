c = sum((5,7))
print(c)
def function1(a,b):
    """this is a doc which we can print using doc whic i will show you . So we should write here about the role of the function so that we can see it using the the doc function."""
    print("thsi is a nice function.")
print(function1.__doc__)
num1 = input()
num2 = input()
try:
    print("sum is", int(num1) + int(num2))
except Exception as e:
    print(e)
print("nice")