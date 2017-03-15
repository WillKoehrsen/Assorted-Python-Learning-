import sys

sys.stderr.write('This is stderr text\n')

sys.stderr.flush()

sys.stdout.write('This is stdout text\n')




if len(sys.argv) > 1:
	print(sys.argv[1:])

def main(arg):
	print(arg)


main(sys.argv[1:])