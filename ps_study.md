# Problem Solving Study



__2021.01.04__ 

_Reviewed_ : `None` 

_Learned_ : Array , Queue

_ToDo_ :  `LeetCode` [933 , 1588 , 1295 , 1304] , `Programmers`  [Printer](https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3) 

---

__2021.01.08__ 

_Reviewed_ :  `LeetCode` [933 , 1588 , 1295 , 1304] , `Programmers`  [Printer](https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3) 

_Learned_ : Stack , Big-O notation

_ToDo_ :   `LeetCode` [682 , 20  ,1603] `Programmers` [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586)

---

__2021.01.11__ 

_Reviewed_ :   `LeetCode` [682 , 20  ,1603] , `Programmers` [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586)

_Learned_ : Linked-List , Tree (before delete)

_ToDo_ :    `LeetCode` [1290,237] , 938 (트리 참고용 문제) , 더블링크 delete function (옵션) 

_ToRead_ : Tree (delete node) , hash concept , 

---

__2021.01.15__ 

_Reviewed_ :  `LeetCode` [1290,237] , 938 (트리 참고용 문제) , 더블링크 delete function (옵션) 

_Learned_ : Tree (delete node) , hash concept , 

_ToDo_ : `LeetCode` [1512(use dict) , 961(use set) , 1207(use dict&set)] , `Programmers` [[완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) (use dict)]   

_ToRead_ : Quick-sort ( + google `Divide and Conquer` if needed)

---

__2021.01.18__ 

_Reviewed_ :  `LeetCode` [1512(use dict) , 961(use set) , 1207(use dict&set)] ,  `Programmers` [[완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) (use dict)]   

_Learned_ : Quick-sort , Recursion

_ToDo_ : 

| Site        | number            | keyword                | hint                                                         |
| ----------- | ----------------- | ---------------------- | ------------------------------------------------------------ |
| LeetCode    | 1710              | desc sort, greedy      | [3,3] 의 박스 정보가 있다고 할때, 3개의 박스를 모두 담을 필요없이 남은 공간이 2라면 2개만 담아도 된다. ( 2박스*3유닛 = 6유닛이 더 추가되는 꼴) |
| LeetCode    | 1370              | desc, asc sort         | 실제로 글자를 하나씩 지우면서 진행하는것이 아니라 각 글자별 회수 dict 를 활용해서 |
| Programmers | 42748(K번째 수)   | sorting multiple times | i , j , k 가 모두 1부터 시작한다는걸 잊으면 안됩니다! 인덱스는 0부터 시작해용 |
| Programmers | 42746(가장 큰 수) | if 문이 특이한 sorting | 11번 테스트 케이스만 틀린다면 다음 반례를 확인하세요 : [0,0,0,0] => "0" |

_ToRead_ : __Binary-Search__ (이진탐색 : 용철) , __Greedy__ (탐욕알고리즘 : 동재)

---

__2021.01.22__ 

_Reviewed_ :  `LeetCode` [1710 , 1370] ,  `Programmers` [[K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748) , [가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746) ]   

_Learned_ : Binary-Search

_ToDo_ : `LeetCode` [852 , 1337 , 167] , 

_ToRead_ : __Greedy__ 

> 참고사항 (2 ways of binary-search with python)

```python
# iterable way

def binary_search_iter(array,data):
    low,high = 0,len(array)-1
    
    while low<high:
        mid = (low+high)//2
        if array[mid]<data:
            low = mid+1
        elif array[mid]>data:
            high = mid
        else:
            return True
        
    return True if array[low]==data else False

# recursive way

def binary_search_recur(array,data):
    
    if len(array)==1:
        if array[0]==data:
            return True
        else:
            return False
    if not len(array):
        return False
    
    mid = len(array)//2
    if array[mid]<data:
        return binary_search_recur(array[mid:],data)
    elif array[mid]>data:
        return binary_search_recur(array[:mid],data)
    else:
        return True
```

---

__2021.02.01__ 

_Reviewed_ :  `LeetCode` [852 , 1337 , 167]

_Learned_ : Greedy

_ToDo_ : `LeetCode` [1221 , 1716(크게 그리디 느낌은 아님 옵션 문제) , 1518 ] , `Programmers` [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862) 

_ToRead_ : __Dynamic Programming__ , __Graph__ 



> 체육복 문제 참고사항

```python
- "reserve" 입력은 sort 되어있지 않음
- 제약사항 5번을 자세히 읽어볼것
```

---

