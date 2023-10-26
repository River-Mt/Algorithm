import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
order = dict()

for i, num in enumerate(S):
    order[num] = i

for i in range(k):
    tmp = [0 for _ in range(len(D))]
    for j in range(len(D)):
        tmp[D[j]-1] = S[j]
    S = tmp

print(*S)


