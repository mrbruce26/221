inp = open("input1b.txt","r")
out = open("output1b.txt","w")
a = inp.readline()
out.write(a)
z = inp.read()
y = z.split("\n")
for i in y:
    h = i.split(" ")
    if(h[2]=="+"):
        out.write(f"The result of {(h[1])} + {h[3]} is {int(h[1])+int(h[3])}\n")
    elif (h[2] == "*"):
        out.write(f"The result of {(h[1])} * {h[3]} is {int(h[1]) * int(h[3])}\n")
    elif (h[2] == "-"):
        out.write(f"The result of {(h[1])} - {h[3]} is {int(h[1]) - int(h[3])}\n")
    elif (h[2] == "/"):
        out.write(f"The result of {(h[1])} / {h[3]} is {int(h[1]) / int(h[3])}\n")