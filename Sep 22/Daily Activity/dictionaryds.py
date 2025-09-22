student = {
    "name" : "Alice",
    "age" : 22,
    "Course" : "AI&ML"
}
print("Name by Index : ",student["name"])
print("Age by get function : ",student.get("age"))



student["Grade"]="A"    # Adding new index

student['age']=23       # Updating existing

print(student)

student.pop("Course")   # remove Course by using pop
print(student)

del student["Grade"]    # Remove by del keyword
print(student)

# Iterating

for key,value in student.items():
    print(f"{key} : {value}")