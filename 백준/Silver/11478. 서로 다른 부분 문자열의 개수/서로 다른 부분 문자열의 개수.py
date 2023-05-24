import sys

s = sys.stdin.readline().rstrip()
dic = {}
s_len = len(s)

for i in range(s_len):
    for j in range(i, s_len):
        sub = s[i:j+1]
        dic[sub] = dic.get(sub, 1)

print(len(dic))
