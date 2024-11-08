inp = open("input.txt","r")
out = open("output.txt","w")
inp.readline()
b = inp.readline().split(" ")
c = inp.readline().split(" ")
print(b)
print(c)
l1=[]
l2 =[]
for i in range(len(b)):
    l1.append(int(b[i]))
    l2.append(int(c[i]))
print(l1)

min_i=0
for i in range(len(l1)):
    min_i = i
    for j in range(i+1,len(l1)):
        if l2[min_i] < l2[j]:
            min_i =j
        elif l2[min_i]==l2[j]:
            if l1[min_i]>l1[j]:
                min_i =j
    temp= l1[i]
    tem = l2[i]
    l1[i] = l1[min_i]
    l2[i] = l2[min_i]
    l1[min_i]=temp
    l2[min_i] = tem
    out.write(f"ID: {l1[i]} Mark: {l2[i]}\n")
print(l1)
print(l2)
