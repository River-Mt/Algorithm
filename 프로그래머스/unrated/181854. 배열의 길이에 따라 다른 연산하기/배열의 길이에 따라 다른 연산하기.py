def solution(arr, n):
    length = len(arr)
    answer = [0] * length
    print(length)
    if length % 2:
        for i in range(length):
            if not i % 2:
                answer[i] = arr[i] + n;
            else:
                answer[i] = arr[i] 
    else:
        for i in range(length):
            if i % 2:
                answer[i] = arr[i] + n;
            else:
                answer[i] = arr[i]
                
    return answer