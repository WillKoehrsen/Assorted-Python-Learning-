import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type = float, default =1.0,
						help= 'What is the first number?')
	parser.add_argument('--y', type = float, default =1.0,
						help= 'What is the second number')
	parser.add_argument('--operation', type = str, default = 'add',
						help= 'What operation?')

	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))


def calc(args):
	# operation = args.operation
	if args.operation == 'add':
		return args.x + args.y
	elif args.operation =='subtract':
		return  args.x - args.y
	elif args.operation =='multiply':
		return  args.x * args.y
	elif args.operation =='divide':
		return  args.x / args.y

# prevents from running if import (as a module) into another script
if __name__ == "__main__":
	main()
