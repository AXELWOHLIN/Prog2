def summa(*args):
    return sum(args)
def maxima(*args):
    return max(args)
def minima(*args):
    return min(args)
def mean(*args):
    return sum(args)/len(args)


print(summa(1,2,3))
print(maxima(3,2,4))
print(minima(2,4,3,1,2))
print(mean(2,2,2))