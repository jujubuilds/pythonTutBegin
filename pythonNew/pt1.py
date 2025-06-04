#this is assigning a bunch of variables with the same value 
x = y = z = "float"
print(x)
#this is the idea of concurrently assinging all of them at the same time
x,y,z = 9.0, 'a', "Aarav"
print(x)
#creating a global variable
someVar = "Hello"
def my_function():
    #modifying global variable value within the function 
    global someVar
    someVar = 9
#this will print Hello since the function has not been called yet
print(someVar)
#now we call the function so the value of the variable has been modified
my_function()
print(someVar)


#Now I will go over some printing techniques
x = "Aarav"
y = 10
z = 10.0
print(x, y, z) #In this technique I will be able to print even though they are of different type
#print(x + y + z) #this will not work 

someList = ['x', 'y', 'd']
d, b, a = someList
print(a)


