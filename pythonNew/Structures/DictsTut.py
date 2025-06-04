#Here is how to initialize a dict
person = {
    "Name": "Aarav",
    "Age" : 19,
    "School" : "Georgia Tech"
}

#Here is how you print a value 
print(person["Name"])
#Here is how you modify a value
person["Age"] = 25
#Here is how you add a new attribute
person["Internship"] = "Amazon"
#Here is how you delete a key
del person["Internship"]
#Here is how you collectively print a dictionary 
print(person)

#Multiple ways to loop thorugh a dictionary
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)

#Creating a lists of Dictionaries
students = [{"Name": "Aarav", "Age" : 19, "Internship": "Amazon"}, {"Name": "Jash", "Age" : 19, "Internship": "Amazon"}]

number = 0
#printing te name of all the students 
for student in students:
    print(student["Name"])
    if(student["Age"] > 18):
        number += 1
students.append({"Name": "Glona", "Age" : 19, "Internship": "N/A"})
print(students)

classroom = {
    "student1" : {"Name" : "Aarav", "Score": 19},
    "student2" : {"Name" : "John", "Score": 20}
}
for key in classroom:
    print(classroom[key])
classroom["student3"] = {"Name": "Buddy", "Score": 30}
classroom["student1"]["Score"] = 95