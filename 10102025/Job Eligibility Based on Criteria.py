def job_eligibility(aptitude, gd, technical, hr):
    total_marks = aptitude + gd + technical + hr
    if total_marks >= 390 and total_marks <= 400:
        salary = 30000
    elif total_marks >= 380 and total_marks < 390:
        salary = 28000
    elif total_marks >= 370 and total_marks < 380:
        salary = 25000
    elif total_marks >= 35 and total_marks < 370:
        salary = 20000
    else:
        salary = 0
    return total_marks, salary

# Get input from user interactively
aptitude_marks = int(input('Enter Aptitude marks: '))
GD_marks = int(input('Enter GD marks: '))
Technical_marks = int(input('Enter Technical marks: '))
HR_marks = int(input('Enter HR marks: '))

marks, offer_salary = job_eligibility(aptitude_marks, GD_marks, Technical_marks, HR_marks)

print('Total Marks:', marks)
print('Offer Salary:', offer_salary)
