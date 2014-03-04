def member_of_nth_fib_lists(listA, listB, needle):
	new_list = []
	if needle == listA:
		return True
	if needle == listB:
		return True
	for i in range(2,len(needle)):
		new_list = listA + listB
		listA = listB
		listB = new_list
		if new_list == needle:
			return True
	else:
		return False


def main():
	print member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])
	print member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4])
	print member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2])
	print member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7])

if __name__ == '__main__':
	main()