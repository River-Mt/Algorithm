import sys
from itertools import combinations
from collections import Counter

t = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
price = []
cnt = []
subs = []
combs = [list(combinations([i for i in range(n)], j + 1)) for j in range(n)]
t_cnt = Counter(t)

for i in range(n):
    p, s = sys.stdin.readline().split()
    price.append(int(p))
    subs.append(s)
    cnt.append(Counter(s))

ans = 1000000000

for comb in combs:
    for nums in comb:
        tmp = ""
        hap = 0
        for num in nums:
            tmp += subs[num]
            hap += price[num]
        c = Counter(tmp)
        flag = False
        for ch in t:
            if c[ch] < t_cnt[ch]:
                flag = True
                break
        if not flag:
            ans = min(ans, hap)
if ans == 1000000000:
    print(-1)
else:
    print(ans)
