import sys

input = sys.stdin.readline
n = int(input())
st = []
ans = 0

for i in range(n):
    h = int(input())
    while st and st[-1] <= h:
        st.pop()
    ans += len(st)
    st.append(h)

print(ans)



