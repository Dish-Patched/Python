a = int(input())
b = []

for i in range(a):
    c = input()
    c = c.split()
    b.append(c)

d = 0
for j in b: #for operating on sublists in a list
    d += float(j[0]) * float(j[1]) 

print(d)

#this program was made for operating on sublists inside a list
