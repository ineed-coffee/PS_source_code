#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    global time_to_str
    
    if not m:
        return time_to_str[h]+" o' clock"
    else:
        paste1=" minute"
        paste2=" past "
        
        if m>30:
            h=(h+1)%12
            m=60-m
            paste2=" to "
        if m>1:
            paste1+="s"
        if m in [15,30]:
            paste1=""
        return time_to_str[m]+paste1+paste2+time_to_str[h]
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())
    m = int(input())
    
    time_to_str={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",
            7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
            13:"thirteen",14:"fourteen",15:"quarter",16:"sixteen",17:"seventeen",18:"eighteen",
            19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",
            24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",
            28:"twenty eight",29:"twenty nine",30:"half"}

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
