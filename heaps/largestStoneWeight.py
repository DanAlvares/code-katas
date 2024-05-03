# https://leetcode.com/problems/last-stone-weight/description/

# Approach: 
# 1. Sort the stones in ascending order.
# 2. Keep popping the last two elements from the list and find the difference.
# 3. If the difference is not zero, then add the difference to the list.
# 4. Sort the list again.
# 5. Repeat the process until the length of the list is 1.
# 6. Return the last element of the list if the list is not empty, else return 0.

def lastStoneWeight(stones):
    stones.sort()
    while len(stones) > 1:
        y = stones.pop()
        x = stones.pop()
        if x != y:
            stones.append(y - x)
            stones.sort()
    return stones[0] if stones else 0