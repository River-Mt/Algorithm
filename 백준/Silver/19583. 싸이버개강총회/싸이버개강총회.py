import sys
input = sys.stdin.readline

s, e, q = input().split()
entered = {}
remained = {}
dic = {}
cnt = 0

while True:
    try: 
        if input == "":
            break
        time, name = input().split()
        if time <= s:
            entered[name] = True
    
        if e <= time <= q:
            remained[name] = True
    except Exception:
        break

for name in entered.keys():
    if remained.get(name):
        cnt += 1

print(cnt)
