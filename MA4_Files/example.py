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
    print(len(lst))
    i = 0
    while i < len(lst):
        a = greater_than_1(lst[i])
        if a:
            lst[i] = a
        else:
            lst.pop(i)
        i += 1
    print(len(lst))
    approx_vol =  len(lst)/n  * (2*d) 
    real_vol = math.pi**(d/2)/(math.gamma(d/2 +1))
    print(f'Approx volume is {approx_vol}')
    print(f'Real volume is {real_vol}')
   # a = [for i in range(0,len(lst)) [list(filter(greater_than_1,lst[j]))) for j in range(0,len(lst))  ] ] 
   # print(a)
    #print(len(a))

def main():
    """
    lst = []
    for k in range(3,6):
    circ(10**k)
    """
    sphere(100000, 7)
if __name__ == '__main__':
    main()
