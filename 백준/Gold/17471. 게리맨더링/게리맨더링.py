import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
ans = 0


def solve():
    global ans
    n = int(input())
    populations = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    max_diff = 100 * n
    ans = max_diff

    def make_graph():
        for i in range(n):
            adj_nodes = list(map(int, input().split()))
            for j in range(1, adj_nodes[0] + 1):
                graph[i].append(adj_nodes[j] - 1)

    def bfs(team):
        dq = deque([])
        chk = [0 for _ in range(n)]
        st = team[0]
        dq.append(st)
        chk[st] = 1
        pop_sum = populations[st]

        while dq:
            cur = dq.popleft()
            for i in range(len(graph[cur])):
                nx = graph[cur][i]
                if chk[nx] or nx not in team:
                    continue
                pop_sum += populations[nx]
                chk[nx] = 1
                dq.append(nx)

        for node in team:
            if chk[node] == 0:
                pop_sum = -1
                break
        return pop_sum

    def is_adjacent(team1, team2):
        global ans
        team1_sum, team2_sum = bfs(team1), bfs(team2)
        if team1_sum == -1 or team2_sum == -1:
            return
        ans = min(ans, abs(team1_sum - team2_sum))

    def separate_team(cur, team1):
        if cur >= n:
            team2 = []
            for node in range(n):
                if node not in team1:
                    team2.append(node)
            if len(team1) == 0 or len(team2) == 0:
                return
            is_adjacent(team1, team2)
            return
        separate_team(cur + 1, team1 + [cur])
        separate_team(cur + 1, team1)

        return

    make_graph()
    separate_team(0, [])

    return ans if ans != max_diff else -1


print(solve())
