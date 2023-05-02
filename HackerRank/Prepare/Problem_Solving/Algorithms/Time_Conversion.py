#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    print(str(s))
    time = (s.split(":"))
    ampm = time[2][2:4]
    if ampm == "PM":
        if time[0] != "12":
            time[0]=int(int(time[0])+12)
            time[0] = str(time[0])
    elif ampm == "AM":
        if time[0] == "12":
            time[0] = "00"
        
    ntime = ':'.join(time)
    print(str(ntime))
    return str(ntime[:-2])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
