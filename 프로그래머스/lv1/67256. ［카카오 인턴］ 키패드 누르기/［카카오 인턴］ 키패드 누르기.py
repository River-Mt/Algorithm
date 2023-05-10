def getDist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution(numbers, hand):
    answer = []
    default_left  = [1, 4, 7]
    default_right = [3, 6, 9]
    middle = [2, 5, 8, 0]
    loc = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)
          }
    
    left_loc = (3, 0)
    right_loc = (3, 2)
    
    for num in numbers:
        if num in default_left:
            left_loc = loc[num]
            answer.append('L')
            
        elif num in default_right:
            right_loc = loc[num]
            answer.append('R')
        
        else:
            num_loc = loc[num]
            left_dist = getDist(num_loc[0], left_loc[0], num_loc[1], left_loc[1])        
            right_dist = getDist(num_loc[0], right_loc[0], num_loc[1], right_loc[1])        

            if left_dist == right_dist:
                if hand == 'right':
                    right_loc = num_loc
                    answer.append('R')
                    
                else:
                    left_loc = num_loc
                    answer.append('L')
                
            elif left_dist < right_dist:
                left_loc = num_loc
                answer.append('L')
            
            else:
                right_loc = num_loc
                answer.append('R')
            
                
    return "".join(answer)