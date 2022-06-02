myset= {"one","two","three","four","five"}
print(myset)
print(len(myset))
print(type(myset))
...
for x in myset:
    print (x)
...
print("two" in myset)
...
myset.add ("yes")
print(myset)
...
a={10,11,12,13}
b={10,20,30,40}
a.update(b)
print (a)
...
a.remove(10)
print(a)
...
a.pop()
print(a)
del(b)
...
b={10,20,30,40,12,13}
c=a.union(b)
print(c)
...
b.intersection_update(a)
print (b)
...
b.symmetric_difference_update(a)
print (b)