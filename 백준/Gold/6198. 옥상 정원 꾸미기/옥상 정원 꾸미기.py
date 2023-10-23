import sys

input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]
st = []
ans = 0

for i, h in enumerate(buildings):
    if not len(st):
        st.append([h, i])
    else:
        while st:
            top_h, top_idx = st[-1]
            if top_h > h:
                break
            ans += i - top_idx - 1
            st.pop()
        st.append([h, i])

for i in range(len(st) - 1):
    ans += st[-1][1] - st[i][1]

print(ans)
