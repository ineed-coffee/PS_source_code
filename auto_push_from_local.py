import os
import subprocess

def reformat(path):
    path_list=path.split("/")
    path_list[-1]= '"'+path_list[-1]+'"'
    return "/".join(path_list)

if __name__ == "__main__":
    try:
        response= subprocess.call("git pull")
    except subprocess.CalledProcessError:
        pass
        
    try:
        response= subprocess.check_output("git status -sb", universal_newlines=True)
    except subprocess.CalledProcessError:
        pass

    files = [path for path in response.split("\n")[1:]]
    py_file = [file[3:] for file in files if file.endswith(".py")]
    sql_file = [file[3:] for file in files if file.endswith(".sql")]

    if py_file:
        try:
            for py in py_file:
                py=reformat(py)
                response= subprocess.check_call(f"git add {py}")
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
