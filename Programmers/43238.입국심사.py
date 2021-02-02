def solution(n, times):
    
    max_total_time = n*max(times)
    
    low,high = 0,max_total_time
    
    while low<high:
        mid = (low+high)//2
        
        processable=sum([mid//i for i in times])
        
        if processable==n:
            break
        
        if processable<n:
            low=mid+1
        else:
            high=mid
        
    new_low,new_high = 0,(low+high)//2
    
    while new_low<new_high:
        new_mid = (new_low+new_high)//2
        
        processable=sum([new_mid//i for i in times])
        
        if processable<n:
            new_low=new_mid+1
        else:
            new_high=new_mid
    
    return new_low
