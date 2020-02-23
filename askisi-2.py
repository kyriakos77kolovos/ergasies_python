f=open("text.txt","r")
line="aa"
i=0
counter1=0
counter2=0
while line!="":
		line=f.readline().strip()
		for i in range (len(line)):
			if ((line[i]=="f") or (line[i]=="c") or (line[i]=="k") or (line[i]=="r")):
				counter1=counter1+1			
			else:
				counter2=counter2+1
				if (line[i]==" "):
					if (counter1>counter2-1):
						print("BAD")
						counter1=0
						counter2=0
					else:
						print("GOOD")
						counter1=0
						counter2=0
if (counter1<=counter2):
	print("GOOD")
else:
	print("BAD")