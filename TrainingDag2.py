from Mymodule import Animal

zebra = Animal("Zoe", 23)

zebra.description()

lion = Animal("Harry", 11)
print(lion.description())

#als ge een functie wilt kunt ge elke keer import math doen en dan functies binnen math gebruiken
import math
print(math.sqrt(36))

#als ge een specifieke functie daarvan vaak gebruikt kan dit ook:
from math import sqrt
print(sqrt(36))

#als ge gwn alle functies wilt importeren omdat dat makkelijker is
from math import *
print(acos(1))
#maar pas op want dan kan het dat ge functies importeert met dezelfde naam als uw functies!!
#Als ge dan al die functies overschrijft worden die van u overschreven!


#code to make it run serial or parallel
 from joblib import Parallel, delayed

import multiprocessing
import time

def myfunction(i):
    print(i)
    time.sleep(2)
    return(i)

if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        myfunction(i)
    print("SERIAL", time.time() - start)

     #parallel timing

    num_cores = multiprocessing.cpu_count()
    print("Number of cores used: "+ str(num_cores))
    start = time.time()
    results = Parallel(n_jobs=num_cores)(delayed(myfunction)(i) for i in range(10))
    print("PARALLEL ", time.time() - start)
    print(results)
