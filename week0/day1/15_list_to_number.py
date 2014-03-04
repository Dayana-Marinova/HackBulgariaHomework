def list_to_number(digits):
	number = 0
	for i in digits:
		number += i
		number *= 10
	number = number / 10
	return number
def main():
	print list_to_number([1, 2, 3, 4])
	print list_to_number([9, 9, 9, 9])
	print list_to_number([1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
	main()