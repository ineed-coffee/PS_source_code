def solution(array, commands):
    answer = []
    
    for (i,j,k) in commands:
        sorted_sub_array = quick(array[i-1:j])
        answer.append(sorted_sub_array[k-1])
    
    return answer

def quick(sub_list):
    
    if len(sub_list)<=1:
        return sub_list
    
    pivot = sub_list[0]
    left = [element for element in sub_list[1:] if element < pivot]
    right = [element for element in sub_list[1:] if element >= pivot]
    
    return quick(left) + [pivot] + quick(right)
