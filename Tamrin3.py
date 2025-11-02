students_list = [
    {
        "student_id": 1,
        "name": "Asal",
        "grades": [18, 19, 20]
    },
    {
        "student_id": 2,
        "name": "Mina",
        "grades": [15, 14, 16.5]
    }
]

def calculate_student_gpa(student_id):
    for student in students_list:
        if student["student_id"] == student_id:
            grades = student["grades"]
            gpa = sum(grades) / len(grades)
            return gpa
    return None

for student in students_list:
    gpa = calculate_student_gpa(student["student_id"])
    print(f"{student['name']} - GPA: {gpa:.2f}")