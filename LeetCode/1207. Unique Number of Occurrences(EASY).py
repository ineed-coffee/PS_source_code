class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        occurrence_dict = {}
        
        for element in arr:
            try:
                occurrence_dict[element]+=1
            except KeyError:
                occurrence_dict[element]=1
                
        values=occurrence_dict.values()
        if len(values)==len(set(values)):
            return True
        return False
