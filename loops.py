from re import X


a=10
b=20
c=30
if a>b:
 print("a is lessthan b")
else:
 print("a is grater than b")
...
if a<b and a>c:
 print ("a is small number")
else:
    print("c is grater number")
...
if a>b:
    print ("a is greater number")
elif b>c:
    print("c is greater number")
else:
    print("a is smaller than b and c")
...
x= 10
y=20
z=10
if x==y:
    print("both are same")
elif x==z:
    print("x and z are same")
else:
    print ("none")
...
##while loops
i=10
while i<=10:
    print(i)
    i+=1
...
i=10
while i<=15:
    print(i)
    i+=1
...

name=("chandana","anusha","chinnu")
for a in name:
    print(a)
...
for x in name:
    print(x)
    if x=="anusha":
        break
...

for x in name:
    if x=="anusha":
        continue
    print(x)
...
##range ()
for x in range(6):
    print(x)
...
for x in range(5,10):
    print (x)
...
for x in range(2,10,3):
    print(x)
...
a= (1,2,3,4)
b=("a","b","c")
for c in a:
    for d in b:
        print (c,d)