def solution(jobs):
    answer,cur_point = 0,0
    N=len(jobs)
    
    def priority(job,cur):
        if cur-job[0]<=0:
            return (job[0],job[1])
        return (-1,job[1])
    
    while jobs:
        jobs.sort(key=lambda x:priority(x,cur_point),reverse=True)
        cur_job=jobs.pop()
        if cur_point-cur_job[0]<=0:
            answer+=cur_job[1]
            cur_point=cur_job[0]+cur_job[1]
        else:
            answer+=cur_job[1]+(cur_point-cur_job[0])
            cur_point=cur_point+cur_job[1]
    
    return answer//N
