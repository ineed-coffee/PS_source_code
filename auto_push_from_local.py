import os
import subprocess

def split(path):
    global abs_path
    path_list=path.split("/")
    name= '"'+path_list[-1]+'"'
    return os.path.join(abs_path,"/".join(path_list[:-1])),name

if __name__ == "__main__":
    abs_path=os.getcwd()
    response= subprocess.call("git pull")
    response= subprocess.call("git add -u")
        
    try:
        response= subprocess.check_output("git status -sb", universal_newlines=True,encoding="utf-8")
    except subprocess.CalledProcessError:
        pass

    files = [path for path in response.split("\n")[1:]]
    py_file = [file[3:] for file in files if file.endswith(".py")]
    sql_file = [file[3:] for file in files if file.endswith(".sql")]

    if py_file:
        try:
            for py in py_file:
                cd,name=split(py)
                print(py)
                print(cd)
                print(name)
                #if cd:
                #    response= subprocess.check_call(f"cd {cd}")
                response= subprocess.check_call(f"git add {name}",cwd=cd)
            response= subprocess.check_call('''git commit -m "daily ps :cloud:"''')
        except subprocess.CalledProcessError:
            print("Error while commiting .py files")

    if sql_file:
        try:
            for sql in sql_file:
                sql=reformat(sql)
                response= subprocess.check_call(f"git add {sql}")
            response= subprocess.check_call('''git commit -m "daily sql :palm_tree:"''')
        except subprocess.CalledProcessError:
            print("Error while commiting .sql files")

    response= subprocess.check_call("git push")
