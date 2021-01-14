class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
                        
        unique_check=set()
        for element in A:
            if element in unique_check:
                return element
            unique_check.add(element)
