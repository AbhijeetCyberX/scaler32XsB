# data structures in a python
# lists
# strings 
a= "hello world"
print(a)
s=input("Enter a message:")
print(s)
# accesing, updating and deleting string elements loops characters
print(s[0])
print(s[4])
#string slicing
print(s[0:2])
print(s[0:1:2])

s= "hello world"
for char  in s:
    print(char)

# string immutability
s= "python is working of the developemts"
s= "A" +s[1:]
print(s)
print(len(s))


# python lists
# creaing a list
# using list
# accessing elements in a list
# adding elements in a list
# insert elements in a list
# removing elements in a list
# extending a list
# updaint a list
print("now here is the list")
a = [12, 11, 122]
print(a)
b=["apple","ball","cat"]
print(b)

# using a list
a = list((1, 2, 3, 'apple', 4.5))  
print(a)
b = list("GFG")
print(b)

# creating a list
a= [13] *2
print (a)

# accesing a list
a=[10,20,30,40]
print(a[0])
print(a[1])
a.append(5)
print(a)
a.insert(1, 2)
print(a)
a.extend([3,4])
print(a)

#updaing element
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

# removing elements
a=[12,122,32]
a.remove(12)
print(a)

# pop
num = [12,132]
num.pop()
print(num)

#tuples
print("another data strucutre is tuples")
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

# curd tuple
tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])
print(tup[:3])

# dictionary
print("dictionary is another data type which is looping")
data = {"name":"Abhijeet",
"role":"cyber security",
"salary":1000000}
print(data)

# accessing  data in dictionary
print(d["name"])
print(d.get("age"))

d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

# set is also another data strucutres
print("adding a set")
s={10, 20,"apple", 50,24}
print(s)
print(type(s))

# accesing a set
s={"a","b",12.12,1}
print(s)
s.add("d",124)
print(s)

#set union and intersection differences 

x={"x", "y"}
y={"x","y","z"}
u=x.union(y)
print(u)

#intersection
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

# differences
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

# list compreshesion
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)