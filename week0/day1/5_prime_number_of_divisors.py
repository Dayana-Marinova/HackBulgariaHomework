def is_prime(n):
	if n < 0:
		n = abs(n)
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2,n):
		if n % i == 0:
			 return False
	else:
		return True

def prime_number_of_divisors(n):
	divisors = 0
	for i in range(1, n+1):
		if n % i == 0:
			divisors += 1
	return divisors

def main():
	print is_prime(prime_number_of_divisors(7))
	print is_prime(prime_number_of_divisors(8))
	print is_prime(prime_number_of_divisors(9))

if __name__ == '__main__':
	main()
