def is_int_palindrom(n):
    if n < 0:
        n = abs(n)
    rev = ""
    for i in str(n):
        rev = i + rev
    if rev == str(n):
        return True
    else:
        return False
