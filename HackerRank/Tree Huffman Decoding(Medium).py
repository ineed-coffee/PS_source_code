"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    pointer=root
    decoded=""
    
    for code in s:
        if code=="1":
            pointer = pointer.right
        elif code=="0":
            pointer = pointer.left
            
        if (pointer.left==None) and (pointer.right==None):
            decoded+=pointer.data
            pointer=root

    print(decoded)
