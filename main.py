# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:03:18 2019

@author: MabuXayda
"""

import sys
import time
from datetime import datetime

def print_example():
    file = open("F:/temp/NordicCoder/python_analysis/test_schedule.txt", "w") 
    current_time = datetime.now()
    file.write("Job start at {}".format(current_time))

if __name__ == "__main__":
    if sys.argv[1] == "test":
        current_time = datetime.now()
        print(current_time)
        time.sleep(200)
    elif sys.argv[1] == "print":
        print_example()