list= [1,2,3,4,5,6,7,5,7,8,9,10]
print (list)
print (len(list))
print (type(list))
print (list[3])
print(list[2:7])
print(list[:8])
print(list[2:])
print (list[-9:-3])
...
list[4] = 11
print(list)
...
if 3 in list :
    print ("yes, it is present in list")
else:
    print ("no, it is not present in the list")
...
list[2:6]= ["a","b","c","d"]
print(list)
...
list.insert(3,"good")
print(list)
...
list.append("hello")
print(list)
...
list.insert(7, 30,)
print(list)
...
list1= ["one","two","three"]
list.extend(list1)
print(list)
...
list .remove("good")
print(list)
...
list.pop(7)
print(list)
...
list1.clear()
print(list1)
...
print(list)
...
list= [1,2,3,4,5,6,7,5,7,8,9,10]
print (list)
...
for x in list:
    print(list)
...
print (range(len(list)))
...
for i in range(len(list)):
    print(list[i])
...
i=0
while i<5:
    print(list[i])
    i+=1
...
i=0
while i<5:
    i+=4
    print(list[i]) 
...
print (list)
list2=list.copy()
print (list2)
...
list3=list1+list2
print (list3)
list1.extend(list2)
