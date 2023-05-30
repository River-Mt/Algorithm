def solution(arr1, arr2):
    lenA = len(arr1)
    lenB = len(arr2)
    
    if lenA != lenB:
        if lenA < lenB:
            return -1
        else: return 1
    
    else:
        if sum(arr1) == sum(arr2):
            return 0
        else: 
            if sum(arr1) < sum(arr2):
                return -1
            else:
                return 1
