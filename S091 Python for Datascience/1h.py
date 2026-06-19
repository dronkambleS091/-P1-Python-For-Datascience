students = {
    "Amit": 85,
    "Riya": 90,
    "Rahul": 78,
    "Rollins": 92,
    "Kartik": 80
}

total = 0

for name, marks in students.items():
    print(name, ":", marks)
    total += marks

average = total / len(students)

top_student = max(students, key=students.get)

print("Class Average:", average)
print("Highest Marks:", top_student, "-", students[top_student])
