ip=input()
mylist=ip.split()
newlist=[]
for i in range(0,len(mylist)):
  if mylist[i] in newlist:
    continue
  else:
      newlist.append(mylist[i])
print(" ".join(newlist))
