import time
from functools import lru_cache
@lru_cache(maxsize = 3)
def s_w(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("now running some work")
    s_w(3)
    print("done")
    s_w(3)
    print("called again")
