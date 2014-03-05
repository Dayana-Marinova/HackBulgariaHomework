import sys

def concat_files(args):
	fname = 'MEGATRON.txt'
	file_mas = []
	for args in range(1,len(sys.argv)):
		file = open(sys.argv[args], 'r')
		file_mas.append(file.read())
		file.close()
	file = open(fname, 'w')
	file.write("\n".join(file_mas))
	file.close()
	return fname


def main():
	concat_files(sys.argv)




if __name__ == '__main__':
	main()
	