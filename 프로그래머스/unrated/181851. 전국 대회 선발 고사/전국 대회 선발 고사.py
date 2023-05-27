def solution(rank, attendance):
    answer = 0
    arr = []
    for i in range(len(rank)):
        if attendance[i]:
            arr.append((rank[i], i))
    s_arr = sorted(arr)[:3]
    
    return s_arr[0][1] * 10000 + s_arr[1][1] * 100 + s_arr[2][1]