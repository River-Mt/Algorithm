import sys

n = int(sys.stdin.readline().rstrip())
dic = {"ChongChong": 1}

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if dic.get(a) or dic.get(b):
        dic[a] = 1
        dic[b] = 1

print(len(dic))
