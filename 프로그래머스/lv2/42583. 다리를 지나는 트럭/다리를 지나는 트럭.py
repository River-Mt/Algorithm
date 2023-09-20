def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    w_sum = 0
    
    while(bridge):
        answer+=1
        w_sum -= bridge.pop(0)
        
        if(truck_weights):
            if(truck_weights[0] + w_sum <= weight):
                w_sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
                
    return answer