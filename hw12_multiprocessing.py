# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:56:29 2021

@author: gendutkiy
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:36:36 2021

@author: gendutkiy
"""
import multiprocessing
import time
import os

print('==================Case Multithreading-fibonacci=================\n\n ')
print(f'jumlah core : {os.cpu_count()}')
start = time.perf_counter()

def find_fibonaci(num):
    list_fibo=[]
    n=0
    b=1
    for a in range(1,num+2) :
        if len(list_fibo) >= 2:
            list_fibo.append(list_fibo[n-1]+list_fibo[n-2])
        else:
            list_fibo.append(b)
        n += 1
    if num in list_fibo:
        print (f'{num} termasuk bilangan fibonacci')
    else:
        print( f'{num} bukan bilangan fibonacci')
    
if __name__ == "__main__":
    tt = [] 
    for i in range(100):
        t = multiprocessing.Process(target=find_fibonaci, args=[i])
        t.start()
        #print(t)
        tt.append(t)
        
    #print(tt)
    
    for j in tt:
        j.join()

    



finish = time.perf_counter()
executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")