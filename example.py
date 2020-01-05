def diff(n):
	temp=str(n) 
	flag=0
	for i in range(0,len(temp)-1):
		if temp[i]-temp[i+1] == 1 or temp[i] - temp[i+1] == -1:
			flag=1
			#list1.append(n)
		else:
			flag=0
	if flag==1:
		list2.append(n)
	return list1
list2=[]
list1=[]
for j in range(0,105):
	if j<=10:
		list2.append(j)
	else:
		v=diff(j)
print(list2)

