import random
import sys
def scramble(filename):
	string=''
	with  open(filename,'r') as f:
		for line in f.readlines():
			words=line.split()
			for word in words:
				i=len(word)
				if i>2:
					word=list(word)
					mid=word[1:-1]
					random.shuffle(mid)
					word[1:-1]=mid
					word="".join(word)
				string+=word+' '
	f.close
	print string
def main():
	args = sys.argv[1:]
	if not args:
		print 'usage: add filename to the end '
		sys.exit(1)
	scramble(args[0])

if __name__=='__main__':
	main()
