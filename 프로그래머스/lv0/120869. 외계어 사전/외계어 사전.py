from itertools import permutations


def is_exist_in_dic(spell, dic):
    perms = permutations(spell)
    for perm in perms:
        s = "".join(perm)
        if s in dic:
            return 1
    return 2
        


def solution(spell, dic):
    return is_exist_in_dic(spell, dic)
  