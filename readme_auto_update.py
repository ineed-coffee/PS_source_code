import re
import os
import json

with open("README.md",'r') as f:
    readme = f.read()
    
with open("readme_auto_update.json") as f:
    update_info=json.load(f)

folder_names=update_info["folder_names"]
Sites=update_info["Sites"]
Links=update_info["Links"]
Patterns = [*map(lambda x : re.compile("\["+x[0]+"\]\("+x[1]+"\)"+"[0-9:a-z ]*"),zip(Sites,Links))]

for idx,pattern in enumerate(Patterns):
    files = os.listdir(os.path.join(os.getcwd(),folder_names[idx]))
    solutions = [file for file in files if file.endswith(".py")]
    readme = pattern.sub("["+Sites[idx]+"]("+Links[idx]+")"+":"+str(len(solutions))+" solutions  ",readme)

with open("README.md",'w') as f:
    f.write(readme) 
