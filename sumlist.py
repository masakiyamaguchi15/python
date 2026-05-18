mylist = [3, 3, 6, 9, 15, 24]
sum=0 #sumを初期化

for element in mylist:
    print(element)
    sum=sum+element

print("合計:",sum)

sum=0 #sumを再度初期化

for i in range(0,len(mylist)):
    print(mylist[i])
    sum=sum+mylist[i]

print("合計:",sum)
