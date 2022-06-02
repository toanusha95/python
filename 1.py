from ast import If
from importlib import import_module
from winreg import HKEY_LOCAL_MACHINE


x = "anusha"
def myfunc():
    x = "good girl"
    print("anusha is" " " + x)
myfunc()
print("anusha is" " " + x)
...
def myfunc():
    global x
    x= "good"
myfunc()
print ("python is" " "+ x)
...
x= "anusha"
def myfunc():
    global x
    x= "good"
myfunc()
print ("python is" " "+ x)
... 
x="1"
y="2"
z="3"
a= float(x)
b= int(y)
c= complex(z)
print (a,b,c)
print (type(a), type(b),type(c))
print (x,y,z)
...

a= "good morning"
print (len(a))
...
a = """My name is anusha,
Iam from wgl,
Iam learning python"""
print (a)
...
a= "hello"
print (a[4])
...
txt = "python is a high level languag"
print ("high" in txt)
...
a = "python is a high level language"
if "good" in a:
 print ("yes,  'high' is present")
else :
 print ("no , it is not present")
...
b= "good morning"
print (b[0])
print (b[3])
print (b[2:5])
print (b[:5])
print (b[2:])
print (b[-7:-2])
...
a= "GooD MorninG FrienD"
print (a. upper())
print (a. lower())
print (a.replace ("M","g"))
print (a.replace ("o","g"))
print (a. split(","))
print (a.replace ("M","g"))