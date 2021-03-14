import re
import os

import subprocess

if __name__ == "__main__":
    try:
        response= subprocess.call("git pull")
    except subprocess.CalledProcessError:
        exit()
        
    try:
        response= subprocess.check_output("git status -sb", universal_newlines=True)
    except subprocess.CalledProcessError:
        exit()

    files = [path for path in response.split("\n")[1:]]
    py_file = [file for file in files if file.endswith(".py")]
    sql_file = [file for file in files if file.endswith(".sql")]

    if py_file:
        try:
            for py in py_file:
                response= subprocess.check_call(f"git add {add}")
            response= subprocess.check_call('''git commit -m "daily ps :cloud:"''')
        except subprocess.CalledProcessError:
            exit()

    if sql_file:
        try:
            for sql in sql_file:
                response= subprocess.check_call(f"git add {add}")
            response= subprocess.check_call('''git commit -m "daily sql :palm_tree:"''')
        except subprocess.CalledProcessError:
            exit()

    response= subprocess.check_call("git push")

