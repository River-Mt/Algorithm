import sys

n = int(sys.stdin.readline().rstrip())
time_lim = 1000005
imos = [0] * time_lim

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    imos[s] += 1
    imos[e + 1] -= 1

psum = [0] * time_lim

for i in range(1, time_lim):
    psum[i] = psum[i - 1] + imos[i]

q = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    print(psum[target])
    