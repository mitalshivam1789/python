import time
from functools import lru_cache
@lru_cache(maxsize = 3)# it will store 3 files in cache memory
def s_w(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("now running some work")
    s_w(3)# it will take time of 3 sec to implement 
    print("done")
    s_w(3)# it will not kate time as the data is stored in cache memory
    print("called again")
