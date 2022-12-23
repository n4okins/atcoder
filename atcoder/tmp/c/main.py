N = int(input())
P = list(map(int, input().split()))
last = P[-1]
for p in range(len(P) - 1, 0, -1):
    if last < P[p]:
        break
    last = P[p]

L, M, R = P[:p], P[p], P[p:]
last = None
R.sort(reverse=True)

R_max = None
while R_max is None:
    if R.index(M) < len(R) - 1:
        R_max = R[R.index(M) + 1]
        break
    R.append(L.pop())

M = R_max
R = set(R)
R.remove(M)
R = list(sorted(R, reverse=True))

if R_max > max(R):
    R_t = R.pop(0)
    R.append(R_max)
    R_max = R_t

R.sort(reverse=True)

print(*L, R_max, *R)
