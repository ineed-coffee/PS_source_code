def solution(m, musicinfos):
    def as_digit(time):
        return int("".join(time.split(":")))
    def time_to_len(start_,end_):
        s_h,s_m=map(int,start_.split(":"))
        e_h,e_m=map(int,end_.split(":"))
        return (e_h*60+e_m)-(s_h*60+s_m)
    def melody_to_digit(melody):
        nonlocal melody_dict,pitch
        for p in pitch:
            melody=melody.replace(p,melody_dict[p])
        return melody
    
    pitch="C#,D#,F#,G#,A#,C,D,E,F,G,A,B".split(",")
    melody_dict={}
    for p in pitch:
        melody_dict[p]=chr(len(melody_dict)+97)
    
    m=melody_to_digit(m)
    for i in range(len(musicinfos)):
        start_,end_,name,melody = musicinfos[i].split(",")
        musicinfos[i]=[as_digit(start_),
                      time_to_len(start_,end_),
                      name,
                      melody_to_digit(melody)]
    
    musicinfos.sort(key= lambda x:(-x[1],x[0]))
    
    Answer='(None)'
    for start_,duration,name,melody in musicinfos:
        n=len(melody)
        played = melody*(duration//n)+melody[:(duration%n)]
        if m in played:
            Answer=name
            break
    return Answer
