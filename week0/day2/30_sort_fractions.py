def sort_fractions(fractions):
	sort_fractions_list = []
	sort_fractions_dic = {}
	result = []
	for items in fractions:
		sort_fractions_dic[float(items[0])/items[1]] = items
		sort_fractions_list.append(float(items[0])/items[1])

	sort_fractions_list.sort()
	for item in sort_fractions_list:
		for key in sort_fractions_dic:
			if item == key:
				result.append(sort_fractions_dic[key])

	return result


def main():
	print sort_fractions([(2, 3), (1, 2)])
	print sort_fractions([(2, 3), (1, 2), (1, 3)])
	print sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])

if __name__ == '__main__':
	main()
