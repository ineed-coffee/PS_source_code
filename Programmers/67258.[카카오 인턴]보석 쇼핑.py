def solution(gems):
    L=len(gems)
    l=len(set(gems))

    low=l-1
    high=L
    start_=0

    while low<high:
        mid=(low+high)//2

        all_covered=False
        check_dict={}
        check_unique=0
        for i in range(L-mid+1):
            if not check_dict:
                for j in range(i,i+mid):
                    check_dict[gems[j]]=check_dict.get(gems[j],0)+1
                check_unique=len(check_dict)
            else:
                check_dict[gems[i-1]]-=1
                if not check_dict[gems[i-1]]:
                    del check_dict[gems[i-1]]
                    check_unique-=1

                if not check_dict.get(gems[i+mid-1],0):
                    check_unique+=1
                    check_dict[gems[i+mid-1]]=1
                else:
                    check_dict[gems[i+mid-1]]+=1

            if check_unique==l:
                all_covered=True
                start_=i
                break

        if not all_covered:
            low=mid+1
        else:
            high=mid

    return [start_+1,start_+low]
