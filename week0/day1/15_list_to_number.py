def list_to_number(digits):
	number = 0
	for i in digits:
		number += i
		number *= 10
	number = number / 10
	return number

print list_to_number([1,2,3,4])