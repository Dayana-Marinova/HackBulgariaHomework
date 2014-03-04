def unique_words_count(arr):
	new_dic = {}
	count = 1
	for i in arr:
		if i in new_dic:
			new_dic[i] += 1
		else:
			new_dic[i] = count
	return len(new_dic)

def main():
	print unique_words_count(["banana", "apple", "apple", "pie", "apple"])
	print unique_words_count(["python", "python", "python", "ruby"])
	print unique_words_count(["HELLO!"] * 10)

if __name__ == '__main__':
	main()