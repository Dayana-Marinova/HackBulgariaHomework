def is_prime(n):
	if n < 0:
		n = abs(n)
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def prime_factorization(n):
	dictionary = {}
	if n > 2:
		for i in range(2,n):
			if n % i == 0:
				dictionary[i] = 0
				while n % i == 0:
					n /= i
					dictionary[i] += 1
	return dictionary


def main():
	print prime_factorization(356)
	print prime_factorization(100)
	print prime_factorization(40)

if __name__ == '__main__':
	main()