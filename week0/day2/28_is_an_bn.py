def is_an_bn(word):
	count_of_a = 0
	count_of_b = 0
	length = len(word)
	if length % 2 != 0:
		return False
	for m in range(0,len(word)):
		if word[m] != 'a' and word[m] != 'b':
			return False
	else:
		rev = ""
		for i in word:
			rev =  i + rev
		for k in range(0,len(word)/2):
			for l in range(0,len(rev)/2):
				if word[k] == rev[l]:
					return False
		else:
			return True


def main():
	print is_an_bn("")
	print is_an_bn("rado")
	print is_an_bn("aaabb")
	print is_an_bn("aaabbb")
	print is_an_bn("aabbaabb")
	print is_an_bn("bbbaaa")
	print is_an_bn("aaaaabbbbb")

if __name__ == '__main__':
	main()