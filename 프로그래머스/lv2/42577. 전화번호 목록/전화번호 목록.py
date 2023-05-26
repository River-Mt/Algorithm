def solution(phone_book):
    answer = True
    dic = {}
    for phone_num in phone_book:
        dic[phone_num] = dic.get(phone_num, phone_num)
    
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            prefix = phone_num[:i]
            if dic.get(prefix):
                 return False
            
    return True