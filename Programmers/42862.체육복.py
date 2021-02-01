def solution(n, lost, reserve):
    common = set(lost)&set(reserve)
    lost = list(set(lost)-common)
    reserve = list(set(reserve)-common)
    students = [1]*n
    reserve.sort()
    for student in lost:
        students[student-1]=0
        
    for student in reserve:
        if not students[student-1]:
            students[student-1]=1
            continue
        if (student-2>=0) and (not students[student-2]):
            students[student-2]=1
        elif (student<=n-1) and (not students[student]):
            students[student]=1 
    
    return sum(students)
