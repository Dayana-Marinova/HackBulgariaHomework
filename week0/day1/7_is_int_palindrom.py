def is_int_palindrom(n):
	if n < 0:
		n = abs(n)
	rev = ""
	for i in str(n):
		rev =  i + rev
	if rev == str(n):
		return True
	else:
		return False

print is_int_palindrom(1)
print is_int_palindrom(42)
print is_int_palindrom(10001)
print is_int_palindrom(999)
print is_int_palindrom(123)