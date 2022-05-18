from person import Person
from time import perf_counter as pc
import matplotlib.pyplot as plt
from numba import njit


def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	
	start = pc()
	print(	fib_py(35) )
	end = pc()
	print(f"Regular python took {end-start} seconds")
	start2 = pc()
	print( fib_numba(35) )
	end2 = pc()
	print(f"Numba python took {end2-start2} seconds")
	start3 = pc()
	p = Person(35)
	print(p.fib())
	end3 = pc()
	print(f"C++ took {end3-start2} seconds")

def fib_py(n):
	if n<= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))
@njit
def fib_numba(n):
	if n<= 1:
		return n
	else:
		return(fib_numba(n-1)+fib_numba(n-2))
if __name__ == '__main__':
	main()
