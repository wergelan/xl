import pandas as pd

def read_excel(fname):
	return pd.read_excel(fname)

def main():
	import sys
	print(list(read_excel(sys.argv[1])))

if __name__ == '__main__':
	main()
