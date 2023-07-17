import sys
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    m = int(input().rstrip())
    f = [-1 for _ in range(n + 1)]
    e = [[] for _ in range(n + 1)]

    def find(u):
        if f[u] < 0:
            return u
        f[u] = find(f[u])
        return f[u]

    def union(u, v):
        u, v = find(u), find(v)
        if u == v:
            return
        if f[u] < f[v]:
            u, v = v, u
        f[v] += f[u]
        f[u] = v

    def union_enemy_with_enemy(u):
        for enemy in e[u]:
            for friend in e[enemy]:
                union(u, friend)

    def count_group():
        cnt = 0
        for i in range(1, n + 1):
            if f[i] < 0:
                cnt += 1
        return cnt

    for i in range(m):
        r, p, q = input().split()
        p, q = int(p), int(q)

        if r == 'E':
            e[p].append(q)
            e[q].append(p)
        else:
            union(p, q)

    for i in range(1, n + 1):
        union_enemy_with_enemy(i)
        
    return count_group()


print(solve())
