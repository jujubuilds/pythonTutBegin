
#Below are numeric types 
#Integers
some_int = 9
#Floats
some_float = 9.0
#Complex numbers
some_comp = 3 + 5j
print(some_comp.real) # will output 3
print(some_comp.imag) # will outptu 5


#Below are Sequence types
soem_String = "Aarav"


#List and all its methods
#They are mutable, you can have all types of different data types, 
#and there exist some different methods that you can run it with explore later
list = ["Aarav", 9.0, 3 + 5j]
#Indexing works as follows
print(list[1])
print(list[-1])#Starts from the back
print(list[1:3])#This is the pratcice of slicing so it will print 1, 2
list.append(5)#adds to the end
list.insert(1, 39) #adds to specified index
list.remove("Aarav")#can remove specific item
list.pop()#you can do something from the back
list.reverse()#you can reverse it
print(len(list))#prints length of list 
for thing in list:
    print(thing)



#tuple. Its essentially an immutbale list
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1]) #will print banana
print(my_tuple[:3])#should print the first three
len(my_tuple)#This will give you the length of a tuple 
print(my_tuple.index("apple"))#gives you index 
print(my_tuple.count("banana"))#tells you the count 


#Range
r = range(5)
print(r)
#range(start, stop, step)