import math

def min_eating_speed(piles, h):
    max_pile = max(piles)
    low = 1
    high = max_pile
    ans = max_pile

    while low <= high:
        mid = (low + high) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
