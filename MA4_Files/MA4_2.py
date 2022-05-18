from person import Person
from time import perf_counter as pc
import matplotlib.pyplot as plt
from numba import njit


def main():
	"""
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib())
	"""
	timeP, timeN, timeC = [],[],[]
	nums = range(30,45)
	for i in nums:
		start = pc()
		fib_py(i)
		end = pc()
		timeP.append(end-start)
		start2 = pc()
		fib_numba(i)
		end2 = pc()
		timeN.append(end2-start2)
		#print(f"Numba python took {end2-start2} seconds")
		start3 = pc()
		p = Person(i)
		p.fib()
		end3 = pc()
		timeC.append(end3-start3)
		#print(f"C++ took {end3-start2} seconds")
	print( timeP)
	print( timeN)
	print( timeC)
	plt.plot(nums,timeP,'ro')
	plt.plot(nums,timeN,'bo')
	plt.plot(nums,timeC,'go')
	plt.show()

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
