def solution(genres, plays):
    best_album = []
    overall_info = {}
    
    for i,(genre,played) in enumerate(zip(genres,plays)):
        try:
            overall_info[genre][0]+=played
            overall_info[genre][1].append((i,played))
        except KeyError:
            overall_info[genre]=[played,[(i,played)]]
    
    order = sorted(overall_info.keys(),key=lambda x : overall_info[x][0],reverse=True)
    for key in order:
        records = overall_info[key][1]
        records.sort(key=lambda x:x[1],reverse=True)
        if len(records)<2:
            for r in records:
                best_album.append(r[0])
        else:
            record1,record2 = records[:2]
            
            if record1[1]==record2[1]:
                if record1[0] < record2[0]:
                    best_album.append(record1[0])
                    best_album.append(record2[0])
                else:
                    best_album.append(record2[0])
                    best_album.append(record1[0])
            else:
                best_album.append(record1[0])
                best_album.append(record2[0])
    
    return best_album
