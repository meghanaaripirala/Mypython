n=int(input("enter the number"))
a = 0
b = 1
count = 0
print("Fibonacci sequence:")
while  a <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b =c
    count += 1
