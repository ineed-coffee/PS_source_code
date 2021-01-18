class Solution:
    def sortString(self, s: str) -> str:
        
        from collections import defaultdict
        
        char_dict = defaultdict(int)
        
        for char_ in s:
            char_dict[char_]+=1
        
        char_unique=list(char_dict.keys())
        
        ascending = self.quick(char_unique,"asc")
        descending = ascending[::-1]
        
        return_string=""
        switch=0
        while True:
            
            if not any(char_dict.values()):break
            
            if not switch:
                for letter in ascending:
                    if char_dict[letter]:
                        return_string+=letter
                        char_dict[letter]-=1

            else:
                for letter in descending:
                    if char_dict[letter]:
                        return_string+=letter
                        char_dict[letter]-=1

            switch = 1-switch

        return return_string
    
    def quick(self,arr,order):
        
        if len(arr)<=1:
            return arr
        
        pivot = arr[0]
        if order=="asc":
            left = [letter for letter in arr[1:] if ord(letter)<ord(pivot)]
            right = [letter for letter in arr[1:] if ord(letter)>=ord(pivot)]
        elif order=="desc":
            left = [letter for letter in arr[1:] if ord(letter)>ord(pivot)]
            right = [letter for letter in arr[1:] if ord(letter)<=ord(pivot)]
        
        return self.quick(left,order)+[pivot]+self.quick(right,order)
        
        
