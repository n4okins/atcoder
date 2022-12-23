N, M = tuple(map(int, input().split()))
R = {n + 1: set() for n in range(N)}
E = list(tuple(map(int, input().split())) for m in range(M))
E.sort()
for a, b in E:
    R[a].add(b)
    R[b].add(a)
for r, v in R.items():
    v = list(sorted(v))
    print(len(v), *v)
