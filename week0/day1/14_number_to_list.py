def number_to_list(n):
	lists = []
	if n < 0:
		n = abs(n)
	while n > 0:
		digit = n % 10
		lists.append(digit)
		n = n // 10
	return lists

print number_to_list(9999)