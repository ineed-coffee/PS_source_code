import re
import os
import json
from collections import deque
import subprocess

def get_files(files,type_):
    return [file for file in files if file.endswith(type_)]

def replace_escapes(arr):
    ret_arr=[]
    escapes=["(",")","[","]","?"]
    replaces=["\(","\)","\[","\]","\?"]
    for element in arr:
        for j,escape in enumerate(escapes):
            element = element.replace(escape,replaces[j])
        ret_arr.append(element)
    return ret_arr

def get_patterns():
    global Sites,Links
    S_replaced = replace_escapes(Sites)
    L_replaced = replace_escapes(Links)
    return [*map(lambda x : re.compile("\["+x[0]+"\]\("+x[1]+"\)"+"[0-9:a-z ]*"),zip(S_replaced,L_replaced))]
    

if __name__ == "__main__":
    with open("README.md",'r') as f:
        readme = f.read()
    
    with open("readme_auto_update.json") as f:
        update_info=json.load(f)

    folder_names=update_info["folder_names"]
    Sites=update_info["Sites"]
    Links=update_info["Links"]
    TYPE_=update_info["TYPE"]
    Patterns = get_patterns()

    for idx,pattern in enumerate(Patterns):
        type_=TYPE_[idx]
        top_path=os.path.join(os.getcwd(),folder_names[idx])
        files = os.listdir(top_path)
        solutions = get_files(files,type_)

        subfolders=deque([file for file in files if os.path.isdir(os.path.join(top_path,file))])
        while subfolders:
            for _ in range(len(subfolders)):
                cur_subfolder=subfolders.popleft()
                cur_path = os.path.join(top_path,cur_subfolder)
                add_files= files = os.listdir(cur_path)
                add_sols = get_files(add_files,type_)
                solutions+=add_sols
                add_subfolders = [file for file in add_files if os.path.isdir(os.path.join(cur_path,file))]
                for folder in add_subfolders:
                    subfolders.append(os.path.join(cur_subfolder,folder))

        readme = pattern.sub("["+Sites[idx]+"]("+Links[idx]+")"+":"+str(len(solutions))+" solutions  ",readme)

    with open("README.md",'w') as f:
        f.write(readme) 
    
    try:
        cur_path=os.getcwd()
        res=subprocess.check_call(f"cd {cur_path}")
        response= subprocess.check_output("git status -sb", universal_newlines=True)
    except subprocess.CalledProcessError:
        exit()

    readme_modified_pattern=re.compile(r"(M).*(README.md)")

    if readme_modified_pattern.search(response):
        print("README.md file modified.")

        try:
            res=subprocess.check_call("git add README.md")
        except subprocess.CalledProcessError:
            exit()

        try:
            res=subprocess.check_call('''git commit -m "readme auto-updated :battery:"''')
        except subprocess.CalledProcessError:
            exit()

        try:
            res=subprocess.check_call("git push")
        except subprocess.CalledProcessError:
            exit()

        print("README.md auto-updated")
    else:
        print("README.md file not modified.")
