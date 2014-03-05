import sys

def main():
	if (sys.argv) > 1:
		filename = sys.argv[1]
		file = open(filename, 'r')
		print (file.read())
	else:
	 	print 'no argv given'

if __name__ == '__main__':
	main()