class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr = [*map(lambda x:(format(x,"b"),format(x,"b").count("1")),arr)]
        arr_answer = self.quick(arr)
        arr_answer = [*map(lambda x:int(x[0],2),arr_answer)]
        return arr_answer
    
    def quick(self,arr):
        
        if len(arr)<=1:
            return arr
        
        pivot = arr[0]
        
        left,right=[],[]
        
        for element in arr[1:]:
            if element[1]>pivot[1]:
                right.append(element)
            elif element[1]<pivot[1]:
                left.append(element)
            else:
                if int(element[0],2)>int(pivot[0],2):
                    right.append(element)
                else:
                    left.append(element)
                    
        return self.quick(left)+[pivot]+self.quick(right)
