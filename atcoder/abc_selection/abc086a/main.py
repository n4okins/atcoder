a, b = list(map(int, input().split()))
a, b = a & 1, b & 1
if a & b:
    print("Odd")
else:
    print("Even")
