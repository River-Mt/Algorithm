import heapq

def h_to_m(arr):
    tmp = []
    
    for st, ed in arr:
        st_h, st_m = map(int, st.split(":"))
        ed_h, ed_m = map(int, ed.split(":"))
        
        tmp.append([st_h * 60 + st_m, ed_h * 60 + ed_m])
    
    return tmp
    
    
def solution(book_time):
    answer = 0
    rooms = 0
    new_book = h_to_m(sorted(book_time))
    pq = [new_book[0][1]]

    for i in range(1, len(new_book)):
        cur_st, cur_ed = new_book[i]
        first_ed = pq[0]
                
        if first_ed + 10 <= cur_st:
            heapq.heappop(pq)
        
        heapq.heappush(pq, cur_ed)

    return len(pq)