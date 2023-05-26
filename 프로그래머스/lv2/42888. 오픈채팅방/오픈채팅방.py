def solution(record):
    answer = []
    user_info = {}
    logs = []
    
    for rec in record:
        tokens = rec.split()
        cmd = tokens[0]
        uid = tokens[1]
        
        if cmd == 'Enter':
            nickname = tokens[2]
            if user_info.get(uid):
                user_info[uid] = nickname
            else:
                user_info[uid] = user_info.get(uid, nickname)

            logs.append((uid, cmd))
            
        elif cmd == 'Leave':
            logs.append((uid, cmd))

        else:
            nickname = tokens[2]
            user_info[uid] = nickname
            
    for log in logs:
        if log[1] == 'Enter':
            answer.append(f'{user_info[log[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{user_info[log[0]]}님이 나갔습니다.')
            
    return answer