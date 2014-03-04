def contains_digit(number, digit):
	if number < 0:
		number = abs(number)
	while number > 0:
		digits = number % 10
		if digits == digit:
			return True
		number = number // 10
	else:
		return False

def contains_digits(number, digits):
	for i in digits:
		dig = contains_digit(number, i)
		if dig == False:
			return False
	return True

def main():

	print contains_digits(12345, [1, 2, 3])
	print contains_digits(402123, [0, 3, 4])
	print contains_digits(666, [6,4])
	print contains_digits(123456789, [1,2,3,0])
	print contains_digits(456, [])

if __name__ == '__main__':
	main()