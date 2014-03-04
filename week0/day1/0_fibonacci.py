def nth_fibonacci(n):
	first = 1
	second = 1
	if n == 1 or n == 2:
		return 1
	else:
		for i in range(2,n):
			n = first + second
			first = second
			second = n
		return n
		
def main():
	print nth_fibonacci(10)
	print nth_fibonacci(2)
	print nth_fibonacci(1)
	print nth_fibonacci(3)

if __name__ == '__main__':
	main()