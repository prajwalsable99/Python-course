# function cache ing
import time
from functools import lru_cache
@lru_cache(maxsize=5)

def work(n):
    
    time.sleep(n)
    return n 


if __name__=="__main__":
    print("in 5 seconds")
    print(work(5))
    print("again")
    print(work(5))
    print("again")
    print(work(5))
    print("again")
    print(work(5))
    print("again")