def reduce_file_path(path):
	new_path = path.split("/")
	result = []

	for item in new_path:
		if item == '..':
			result.pop()
		elif item == '.':
			pass
		elif item != '':
			result.append(item)
	return '/' + '/'.join(result)


def main():
	print reduce_file_path("/srv/www/htdocs/wtf/")
	print reduce_file_path("/srv/./././././")
	print reduce_file_path("/etc//wtf/")
	print reduce_file_path("/etc/../etc/../etc/../")
	print reduce_file_path("/home/didi/lesson/../")

if __name__ == '__main__':
	main()