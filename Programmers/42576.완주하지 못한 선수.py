def solution(participant, completion):
    
    participant_dict={}
    completion_dict={}
    
    for person in participant:
        try:
            participant_dict[person]+=1
        except KeyError:
            participant_dict[person]=1
            
    for person in completion:
        try:
            completion_dict[person]+=1
        except KeyError:
            completion_dict[person]=1
    
    for key in participant_dict:
        
        try:
            if participant_dict[key]==completion_dict[key]:
                continue
            return key
        except KeyError:
            return key
