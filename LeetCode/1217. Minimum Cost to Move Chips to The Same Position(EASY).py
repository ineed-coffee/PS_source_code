class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int: 
        evens=[1 for pos in position if not pos%2]
        return min(sum(evens),len(position)-sum(evens))
