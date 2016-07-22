def fib(n):
	if n<3:
		return 1
	a=1
	b=1
	i=2
	while i<n:
		temp=a+b
		a=b
		b=temp
		i+=1
	return b
def main():
	n=input("Element Number: ")
	val=fib(n)
	print "The "+str(n)+"th element is",val
if __name__=="__main__":
	main()
