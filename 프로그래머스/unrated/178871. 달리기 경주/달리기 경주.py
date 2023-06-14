def solution(players, callings):
    dic = {}
    idx = 0
    
    for p in players:
        dic[p] = idx
        idx += 1
        
    for name in callings:
        prev , cur = dic[name] - 1 , dic[name]
        players[prev], players[cur] = players[cur] , players[prev]
        dic[players[prev]] , dic[players[cur]] = dic[players[prev]] - 1 , dic[players[cur]] + 1
        
    return players