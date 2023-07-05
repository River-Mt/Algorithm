def reverse_arrays(deliveries, pickups):
    deliveries.reverse()
    pickups.reverse()

    
def solution(cap, n, deliveries, pickups):
    answer = 0
    reverse_arrays(deliveries, pickups)
    
    idx = 0
    d_sum = 0
    p_sum = 0

    while idx < n:
        d_sum += deliveries[idx]
        p_sum += pickups[idx]    
        
        while d_sum > 0 or p_sum > 0:
            d_sum -= cap
            p_sum -= cap
            answer += (n - idx) * 2 

        idx += 1
    
    return answer