from itertools import combinations as com


def answer(num_buns, num_required):
    bunnies = [[] for i in range(num_buns)]
    if num_required == 0:
        return bunnies
    start = 0
    for c in com(bunnies, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        start += 1
    return bunnies
