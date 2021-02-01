class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        from collections import defaultdict
        
        num_dict = defaultdict(list)
        for i,num in enumerate(numbers):
            num_dict[num].append(i)
        
        same_val = False
        for i,num in enumerate(numbers):
            if target-num in num_dict:
                if target-num==num:
                    if len(num_dict[num])>1:
                        one=i
                        same_val=True
                        break
                    else:
                        continue
                else:
                    one=i
                    break
        
        if same_val:
            if (one-1>=0) and (numbers[one-1]==numbers[one]):
                the_other = one-1
            elif (one+1<=len(numbers)-1) and (numbers[one+1]==numbers[one]):
                the_other = one+1
        else:
            the_other = self.find_the_other(numbers[:one]+numbers[one+1:],target-numbers[one])
            if the_other>=one: the_other+=1
                
        return sorted([one+1,the_other+1])
    
    def find_the_other(self,arr,target):
        
        low,high = 0,len(arr)-1
        
        while low<high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid
        
        return low
            
        
