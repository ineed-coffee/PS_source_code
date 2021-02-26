import sys
from collections import defaultdict

def solve(orders,course):

    def all_course_possible(list_,idx,course): # combination implementation with back-tracking
        nonlocal course_len,cur_courses,visited

        if len(course)==course_len:
            key = "".join(sorted(course)) # ★★
            cur_courses[key]+=1
            return

        for i in range(idx,len(list_)):
            if not visited[i]:
                visited[i]=True
                all_course_possible(list_,i,course+list_[i])
                visited[i]=False
        return

    Answer=[]
    for course_len in course:
        if len([order for order in orders if len(order)>=course_len])<2: #at most 1 person ordered this long
            break

        cur_courses=defaultdict(int)
        for order in orders:
            visited=[False]*len(order)
            all_course_possible(order,0,"")

        cur_course_items = cur_courses.items()
        top_freq = sorted(cur_course_items,key=lambda x:x[-1])[-1][-1]
        if top_freq==1: # at most 1 person ordered this combination(course)
            break
        for k,v in cur_course_items:
            if v==top_freq:
                Answer.append(k)

    return sorted(Answer)
    
if __name__ == "__main__" :

    in1 = ["ABCFG AC CDE ACDE BCFG ACDEH",
           "ABCDE AB CD ADE XYZ XYZ ACD",
           "XYZ XWY WXA"]
    in2 = [[2,3,4],
           [2,3,5],
           [2,3,4]]
    out = ["AC ACDE BCFG CDE",
           "ACD AD ADE CD XYZ",
           "WX XY"]

    for i,(orders,course,result) in enumerate(zip(in1,in2,out)):
        orders = orders.strip().split()
        result = result.strip().split()
        print(f"testcase {i+1}:")
        print(f"input    :{orders},{course}")
        print(f"expected :{result}")
        print(f"yours    :{solve(orders,course)}")
        print("="*35)
