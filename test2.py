import re
import os
import json

if __name__ == "__main__":
    with open("status.txt",'r') as f:
        status = f.read()

    readme_modified_pattern=re.compile(r"(M).*(README.md)")
    if readme_modified_pattern.search(status):
        with open("commit_or_not.txt","w") as f:
            f.write("1")
    else:
        with open("commit_or_not.txt","w") as f:
            f.write("0")
