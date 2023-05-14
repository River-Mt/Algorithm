from itertools import product
def solution(word):
    answer = 0
    li = ['A', 'E', 'I', 'O', 'U']
    order = []
    for i in range(1, 6):
        for w in product(li, repeat=i):
            order.append(''.join(list(w)))

    order.sort()
    answer = order.index(word) + 1
    return answer