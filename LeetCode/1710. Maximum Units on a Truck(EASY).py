class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units=0
        sorted_box = self.quick(boxTypes)
        
        for box in sorted_box:
            
            if box[0]>=truckSize:
                units += truckSize*box[1]
                truckSize=0
            else:
                units += box[0]*box[1]
                truckSize-=box[0]
                
            if not truckSize: break
        
        return units
    
    
    def quick(self,list_):
        
        if len(list_)<=1:
            return list_
        
        pivot_cnt = list_[0][0]
        pivot = list_[0][1]
        
        left = [element for element in list_[1:] if element[1]>pivot]
        right = [element for element in list_[1:] if element[1]<=pivot]
        
        return self.quick(left)+[[pivot_cnt,pivot]]+self.quick(right)
        
