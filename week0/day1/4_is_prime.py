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
print is_prime(1)
print is_prime(2)
print is_prime(4)
print is_prime(11)
print is_prime(-10)
