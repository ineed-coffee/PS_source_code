import re
import os
import json
from collections import deque

with open("README.md",'r') as f:
    readme = f.read()
    
with open("readme_auto_update.json") as f:
    update_info=json.load(f)

folder_names=update_info["folder_names"]
Sites=update_info["Sites"]
Links=update_info["Links"]
Patterns = [*map(lambda x : re.compile("\["+x[0]+"\]\("+x[1]+"\)"+"[0-9:a-z ]*"),zip(Sites,Links))]

for idx,pattern in enumerate(Patterns):
    top_path=os.path.join(os.getcwd(),folder_names[idx])
    files = os.listdir(top_path)
    solutions = [file for file in files if file.endswith(".py")]

    subfolders=deque([file for file in files if os.path.isdir(os.path.join(top_path,file))])
    while subfolders:
        for _ in range(len(subfolders)):
            cur_subfolder=subfolders.popleft()
            cur_path = os.path.join(top_path,cur_subfolder)
            add_files= files = os.listdir(cur_path)
            add_sols = [file for file in add_files if file.endswith(".py")]
            solutions+=add_sols
            add_subfolders = [file for file in add_files if os.path.isdir(os.path.join(cur_path,file))]
            for folder in add_subfolders:
                subfolders.append(os.path.join(cur_subfolder,folder))
    
    readme = pattern.sub("["+Sites[idx]+"]("+Links[idx]+")"+":"+str(len(solutions))+" solutions  ",readme)

with open("README.md",'w') as f:
    f.write(readme) 
