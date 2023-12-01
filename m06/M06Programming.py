# Charles Tranter
# SDEV220
# Module 6 programming assignemt
# 12/1/2023

import time
from datetime import datetime
import multiprocessing as mp
import random


# The definiton and the main loop for 15.1 had to be moved because when a process was called, 
# it kept running the code for 13.1 - 3

def print_time():
    wait = random.random()
    time.sleep(wait)
    print(datetime.now())

if __name__ == "__main__":

    # 13.1 - 2

    file = open("today.txt","r")
    today_string = file.read()
    file.close()
    print(today_string)

    # 13.3 - Not entirely sure if this is what the the assignment is asking for as the question is a little vague.

    format = "%m/%d/%Y"
    today = time.strptime(today_string, format)
    print(time.strftime(format, today))



    # 15.1


    for i in range(3):
        process = mp.Process(target=print_time)
        process.start()
        process.join()


    
    
   
