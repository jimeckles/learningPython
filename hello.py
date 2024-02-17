import sys

x = 1

if(x==1):
    print("Hello World1")
else:
    print("not")

myfloat = float(4)
mystring = "this is it"
print(myfloat)

mixer = str(myfloat) + mystring
print(mixer)

v1, v2 = 4.5, "hello"
print(v1)

if(isinstance('flower', float)):
    print("hello is float")
else:
    print('hello is not float')

myList = ['a', 'b', 'c', 1.2, 3]

myList.append('end')
for x in myList:
    print(x)

print("the second item is %s" % myList[1])
print("the list .toString() is %s" % myList)


number = 1 + 2 * 3 / 4.0
print(number)
print(2 * 3 / 4.0)
print(3 / 4.0)

print("mutiply strings fun %s" % "hello " * 5)

l1,l2 = [1,2],[3,4]
l3=l1+l2
print("add arrays using + %s" % l3)
print("add arrays using + %s" % ([1,2]+[3,4]))

print("repeating %s" % l3*4)

x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

x_list = x_list*10
y_list = y_list*10
big_list=x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

print("hello %s is %d" % ('bob', 3.4))

print(len('this'))

print("this is it".index('s'))

print("slice a string %s" % "this is it"[1:-1])
print("slice a string %s" % "this is it"[1:-1:2])#[start:stop:step].
print("reverse a string % s" % "reverse a string"[::-1])
print("to upper %s" % "to upper".upper())

