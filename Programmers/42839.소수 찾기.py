def solution(numbers):

    from itertools import permutations

    raw_join_set = set()
    prime_set = set()
    
    for i in range(1,len(numbers)+1):
        orders = [*map(list,permutations(numbers,i))]
        
        for order in orders:
            raw = int("".join(order))
            
            if raw<2:
                continue
            
            if raw not in raw_join_set:
                raw_join_set.add(raw)
                if raw<10:
                    if (raw==2) or (raw==3):
                        prime_set.add(raw)
                    if raw%2 and raw%3:
                        prime_set.add(raw)
                else:
                    flag=True
                    for i in range(2,int(raw**0.5)+2):
                        if not raw%i:
                            flag=False
                            break
                    if flag: prime_set.add(raw)
                    
    return len(prime_set)
