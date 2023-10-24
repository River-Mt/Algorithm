
class UnionFind:
    def __init__(self, n):
        self.p = [-1 for _ in range(n)]

    def find(self, u):
        if self.p[u] < 0:
            return u
        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)

        if u == v:
            return

        if self.p[u] > self.p[v]:
            u, v = v, u

        self.p[u] += self.p[v]
        self.p[v] = u


n = int(input())
m = int(input())
uf = UnionFind(n)

arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if arr[i][j]:
            uf.union(i, j)
chk = set()

for num in list(map(int, input().split())):
    chk.add(uf.find(num-1))

if len(chk) > 1:
    print("NO")
else:
    print("YES")



