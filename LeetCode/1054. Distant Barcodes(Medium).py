class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        cnt_dict={}
        for b in barcodes:
            cnt_dict[b]=cnt_dict.get(b,0)+1
        
        key_sort=sorted(cnt_dict.keys(),key=lambda x:cnt_dict[x],reverse=True)
        
        B=len(barcodes)
        K=len(key_sort)
        cnt,idx,ans=0,0,[]
        while cnt<B:
            if not cnt_dict[key_sort[idx]]:
                idx=0
                continue
            elif ans and (ans[-1]==key_sort[idx]):
                side=0
                for i,c in enumerate(ans):
                    if int(c)==key_sort[idx]:
                        side=0
                    else:
                        side+=1
                        if side==2:
                            break
                ans=ans[:i]+[key_sort[idx]]+ans[i:]
            else:
                ans.append(key_sort[idx])
            cnt_dict[key_sort[idx]]-=1
            cnt+=1
            idx=(idx+1)%K
        return ans
        
