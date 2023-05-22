import sys

n = int(sys.stdin.readline().rstrip())
A = sys.stdin.readline().rstrip().split()
dic = {}

for name in A:
    dic[name] = dic.get(name, 0)

for i in range(n):
    names = sys.stdin.readline().rstrip().split()
    for name in names:
        dic[name] = dic.get(name) + 1

sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

for name, cnt in sorted_dic:
    print(name, cnt)
    