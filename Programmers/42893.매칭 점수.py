import re

def solution(word, pages):
    sites_adj={}
    bodies={}
    answer=0
    cur_page_url=re.compile('''(<meta property="og:url" content=")(?P<cur_url>.*)("/>)''')
    links_pat=re.compile(r'''(<a href=")(?P<links>.+?)(")''')
    a_pat=re.compile(r"(<a)(?P<links>.*)(></a>)")
    a_pat=re.compile(r'''<a href=".+?></a>''')
    body_pat=re.compile("(<body>)(?P<body_txt>.*)(</body>)",re.DOTALL)
    
    for i,page in enumerate(pages):
        url=cur_page_url.search(page)
        url=url.group("cur_url")
        if not sites_adj.get(url,[]):
            sites_adj[url]=[[],[],i]
        sites_adj[url][-1]=i
            
        links=[i[1] for i in links_pat.findall(page)]
        
        for link in links:
            if not sites_adj.get(link,[]):
                sites_adj[link]=[[],[],1000]
            sites_adj[url][0].append(link)
            sites_adj[link][1].append(url)
        
        body_txt=body_pat.search(page).group("body_txt")
        body_txt=a_pat.sub(" ",body_txt)
        body_txt=re.sub("[^a-zA-Z]"," ",body_txt)
        body_txt=body_txt.split()
        body_txt=[w.lower() for w in body_txt]
        bodies[url]=body_txt
    
    site_score={}
    for key_ in sites_adj.keys():
        site_score[key_]=[0,0,0,0,sites_adj[key_][-1]]
        if bodies.get(key_,0):
            site_score[key_][0]=len([w for w in bodies[key_] if w==word.lower()])
        else:
            site_score[key_][0]=0
        site_score[key_][1]=len(sites_adj[key_][0])
        
    for key_ in site_score:
        for link in sites_adj[key_][1]:
            if site_score[link][1]:
                site_score[key_][2]+=site_score[link][0]/site_score[link][1]
    
    for key_ in site_score:
        site_score[key_][3]=site_score[key_][0]+site_score[key_][2]
        
    answer=sorted(site_score.values(),key=lambda x:(x[-2],-x[-1]))[-1][-1]
        
    return answer
