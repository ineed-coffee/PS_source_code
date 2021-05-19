class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ret = []
        
        dup_dict = {}
        
        for info in paths:
            dir_,*files = info.split(" ")
            for file in files:
                name,content = file.split("(")
                if dup_dict.get(content[:-1],-1)==-1:
                    dup_dict[content[:-1]]=[]
                dup_dict[content[:-1]].append(dir_+"/"+name)
        
        for k,v in dup_dict.items():
            if len(v)>1 : ret.append(v)
                
        return ret
        
