year = int(input("Enter year: "))
semester = int(input("Enter semester: "))

subjects = {
    (1, 1): ["Maths", "Physics", "Chemistry", "English", "CS"],
    (1, 2): ["Maths II", "Physics II", "Biology", "English II", "CS II"],
    (2, 1): ["Discrete Maths", "Algorithms", "Electronics", "Programming", "Databases"],
}

key = (year, semester)
if key in subjects:
    print("Subjects:", ', '.join(subjects[key]))
else:
    print("Subjects not found for given year and semester.")
