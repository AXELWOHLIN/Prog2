"""
Solutions to module 1
Student: AXEL WOHLIN
Mail: axelwohlin@gmail.com
Reviewed by: ALICIA ROBERTSSON
Reviewed date: 31/3
"""


import random
import time


def power(x, n):         # Optional
    pass

def multiply(m, n):  
        # Compulsory
    if n==0:
        return 0
    elif n == 1:
      return m
    else:
        return m + multiply(m,n-1)


def divide(t, n):        # Optional
    pass


def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):
    b = a.copy()
    if len(b) == 1:
      return b[0]
    elif b[0]<b[1]:
        return largest(b[1:])
    else:
      b.pop(1)
      return largest(b)


def count(x, s):   # Compulsory #GÖR OM
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        if type(s[0]) == list and s[0] == x:
            return 1
        elif type(s[0]) == list:
            return count(x,s[0])
        elif s[0] == x:
            return 1
        else:
            return 0
    elif type(s[0]) == list:
      return count(x,s[0]) + count(x,s[1:])
    else:
        if s[0] == x:
            return 1 + count(x,s[1:])
        else:
            return count(x,s[1:])

 
    
def zippa(l1, l2):   # Compulsory
    if len(l2)== 0:
        return l1
    elif len(l1) == 0:
        return l2
    else:
        return [l1[0]] + zippa(l2,l1[1:])

    
def bricklek(f, t, h, n): # Compulsory
    """

    """
    if n==0:
        return []
    elif n == 1:
        return [f+"->"+t]
    else:
        return bricklek(f,h,t,n-1) + [f+"->"+t] + bricklek(h,t,f,n-1)

def fib ( n ) :
    if n == 0 :
      return 0
    elif n == 1 :
      return 1
    else :
      return fib ( n - 1 ) + fib ( n - 2 )

def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    print(multiply(5,5))
    print(harmonic(3))
    print(largest([6,9,12,10,600,6000]))
    print(count(4,[] ))
    print(zippa([1, 3, 5], [ 2, 4, 6, 8, 10]))
    print(bricklek('f', 't', 'h', 6))

    import time
    tstart1 = time . perf_counter ()
    fib(10)
    tstop1 = time . perf_counter ()
    print(f" Measured time : { tstop1 - tstart1 } seconds " )

    tstart = time . perf_counter ()
    fib(20)
    tstop = time . perf_counter ()
    print( f" Measured time : { tstop - tstart } seconds " )
    print((tstop - tstart) / (tstop1 - tstart1) )
    print( (1.6**20) / (1.6**10))

    tstart50 = time . perf_counter ()
    fib(30)
    tstop50 = time . perf_counter ()
    print( f" Tid för fib(30) är : { tstop50 - tstart50 } seconds " )
if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  Eftersom att komplexiteten för antalet brickförflyttningar ges av 2**n - 1
  (enligt kursmaterialet) så kommer antalet brickförflyttningar vid brickleken med 50 brickor 
  att vara 2**50 - 1 förflyttningar. Om en förflyttning tar 1 sekund kommer därför tiden för
  hela brickleken med 50 brickor att ta 2**50 - 1 sekunder, eller 1125899906842623 sekunder, som
  är 357020518 år.
  Precis som för Hanois torn så ser vi att brickleken med många antal brickor är hopplöst att beräkna.

  

  Exercise 17: Time for Fibonacci:
  a) Jag har visat i main att ökningen i beräkningstid verkligen stämmer överens med komplexiteten.
  b) tiden för fib(50) på min dator visas i main. För att uppskatta tiden fib(100) hade tagit kan
  vi multiplicera tiden för fib(50) med (1.6**100)/(1.6**50).

  Tid för fib(30): 1.85sek
  Uppskattad tid för fib(50): 1.85*(1.6**50)/(1.6**30)
  Uppskattad tid för fib(100): 1.85*(1.6**100)/(1.6**30)
  
  
  Exercise 20: Comparison sorting methods:
  1000 = 10**3
  merge(10**3) = 1 sek, theta(n*log(n))
  instick(10**3) = 1 sek, theta(n**2)

  Vi får då att
  merge(10**6) = 1 sek * 1000*log(1000)
  instick(10**6) = 1 sek * 1000**2
  merge(10**9) = 1 sek * 10**6*log(10**6)
  instick(10**9) = 1 sek * (10**6)**2
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  A solves problem in n-long d-struct in n seconds -> A theta(n)
  B solves order theta(c*n*log(n)), time for B for n == 10 -> 1 sek

  Solve for constants in B: c*10*log(10) = 1, we use log base 10 to simplify
                            c = 1/10

Now solve inequality:
1/10*n*log(n) > n 
log(n) > 10 
solutions are all n > 10**10
  

"""