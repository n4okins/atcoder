N = int(input())
a = list(map(int, input().split()))
R = -1

def can(an):
    return (an // 2 == an / 2) or (an // 3 == an / 3)

def

print(any(map(can, a)))
