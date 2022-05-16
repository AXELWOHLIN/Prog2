from re import A
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import random
import math
import matplotlib.pyplot as plt
import functools

def circ(n):
    nc = 0
    insideX, insideY = [],[]
    outsideX, outsideY = [],[]
    for _ in range(1,n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            nc += 1
            insideX.append(x)
            insideY.append(y)
        else:
            outsideX.append(x)
            outsideY.append(y)
    print(str(nc) + ' punkter hamnade i cirkeln')
    print('pi är approx ' + str(4*nc/n))
    print(math.pi)
    plt.plot(insideX,insideY,'ro')
    plt.plot(outsideX,outsideY,'bo')
    plt.show()

def sphere(n,d):
    def greater_than_1(input_list):
        lst = [ele**2 for ele in input_list]
        if sum(lst) <= 1:
            return lst
        else:
            return None

    r = 1
    lst = [[random.uniform(-1,1) for _ in range(0,d)] for e in range(1,n)]
    i = 0
    b = len(lst)
    while i < len(lst):
        a = greater_than_1(lst[i])
        if a:
            lst[i] = a
            i += 1
        else:
            lst.pop(i)
    approx_vol =  len(lst)/n * ((2*r)**d) 
    real_vol = math.pi**(d/2)/(math.gamma(d/2 +1))
    print(f'Approx volume is {approx_vol}')
    print(f'Real volume is {real_vol}')

def main(): 
    """
    lst = []
    for k in range(3,6):
    circ(10**k) 
    """
    #sphere(100000, 11)
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        a = [100000]
        b = [11]
        p1 = []
        p2 = []
        for _ in range(10):
            p1 = p1+a
            p2 = p2+b
        results = ex.map(sphere,p1,p2)
    end = pc()
    print(f"10-parrallel processer tog {round(end-start, 2)} sekunder")

    start = pc()
    with future.ProcessPoolExecutor() as ex:
            result = ex.submit(sphere,1000000,11)
    end = pc()
    print(f"1 stor process tog {round(end-start, 2)} sekunder")
if __name__ == '__main__':
    main()