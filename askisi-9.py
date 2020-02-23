num=input("Enter number: ")
finalnum=num
sum=10
while sum>9:
	sum=0
	finalnum=finalnum*3+1
	while finalnum!=0:
		sum=sum+finalnum%10
		finalnum=finalnum/10
	if finalnum==0:
		finalnum=sum
print(sum)