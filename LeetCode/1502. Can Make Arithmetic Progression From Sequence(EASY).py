class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        diff="yet"
        for i in range(len(arr)-1):
            if type(diff) == str:
                diff=arr[i]-arr[i+1]
                continue
            if diff!=arr[i]-arr[i+1]:
                return False
        return True
        
