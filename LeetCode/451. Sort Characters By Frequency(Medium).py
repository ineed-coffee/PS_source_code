class Solution:
    def frequencySort(self, s: str) -> str:
        from heapq import heapify,heappop
        freq_dict = {}
        for i,letter in enumerate(s):
            if letter not in freq_dict:
                freq_dict[letter]=[i,1]
                continue
            freq_dict[letter][1]+=1
            
        freq_list =[(-cnt,idx,k)  for k,(idx,cnt) in freq_dict.items()]
        answer=""
        heapify(freq_list)
        while freq_list:
            cnt,idx,letter=heappop(freq_list)
            answer+=letter*(-cnt)
        return answer
        
