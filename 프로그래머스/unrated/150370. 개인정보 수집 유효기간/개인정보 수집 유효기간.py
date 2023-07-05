def solution(today, terms, privacies):
    answer = []
    days = {}
    idx = 1
    ty, tm, td = map(int, today.split("."))
    for term in terms:
        tp, day = term.split();
        days[tp] = int(day)

    for privacy in privacies:
        dt, tp = privacy.split()
        y, m, d = map(int, dt.split("."))
        m += days[tp]
        while m > 12:
            y += 1
            m -= 12
       
        s = ""
        
        s += str(y) + "."
        if m < 10:
            s += "0" + str(m) + "."
        else:
            s += str(m) + "."
        if d < 10:
            s += "0" + str(d)
        else:
            s += str(d)
        
        if today >= s:
            answer.append(idx)
    
        idx += 1

    return answer