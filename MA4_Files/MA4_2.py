from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	ans = 1 +2 
	return ans
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
