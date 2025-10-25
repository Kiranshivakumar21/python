total_classes = int(input("Enter number of total_classes: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percent = (classes_attended / total_classes) * 100
print("Percentage of classes attended:", attendance_percent)

if attendance_percent >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")
