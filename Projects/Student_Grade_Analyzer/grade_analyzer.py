name = input("Enter student name: ")

subjects = []
marks = []

for i in range(1, 6):
    subject = input(f"Enter subject {i} name: ")

    while True:
        mark = float(input(f"Enter marks for {subject}: "))

        if 0 <= mark <= 100:
            subjects.append(subject)
            marks.append(mark)
            break
        else:
            print("Please enter marks between 0 and 100.")

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

status = "Pass" if percentage >= 40 else "Fail"

print("\n----- Result -----")
print("Student:", name)

for i in range(5):
    print(subjects[i] + ":", marks[i])

print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Status:", status)
