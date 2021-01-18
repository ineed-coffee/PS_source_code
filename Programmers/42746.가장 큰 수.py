def solution(numbers):
    sorted_numbers = quick(numbers)
    answer = ''
    
    for num in sorted_numbers:
        answer+=str(num)
        
    while answer[0]=="0":
        answer = answer[1:]
        if len(answer)==1:break
        
    return answer

def quick(arr):
    
    if len(arr)<=1:
        return arr
    
    pivot = arr[0]
    pivot_L = len(str(pivot))
    left,right=[],[]
    
    for element in arr[1:]:
        
        if element == 0:
            right.append(element)
        elif pivot == 0:
            left.append(element)
                
        else:
            if int(str(element)+str(pivot))>int(str(pivot)+str(element)):
                left.append(element)
            else:
                right.append(element)
    
    return quick(left)+[pivot]+quick(right)
