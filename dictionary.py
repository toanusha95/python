mydict= {
    "name": "anusha",
    "class": "ssc",
    "from": "plk"
}
print(mydict)
print(len(mydict))
print(type(mydict))
...
x=mydict["name"]
print (x)
...
x=mydict.keys()
print(x)
mydict["year"]="2020"
print (mydict)
y=mydict.values()
z=mydict.items()
print(y)
print(z)
mydict.update({"year":1919})
print (z)
mydict["college"]="svs"
print (z)
