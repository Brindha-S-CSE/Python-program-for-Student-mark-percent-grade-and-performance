name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input("Enter mark for subjects{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
        grade="A+"
        performance="Outstanding"
elif percentage>=80:
        grade="A"
        percentage="Excellent"
elif percentage>=70:
        grade="B"
        percentage="Very good"
elif percentage>=60:
        grade="C"
        percentage="Good"
elif percentage>=50:
        grade="D"
        performance="Average"
else:
        grade="F"
        performance="Needs improvement"
print("/n---Academic Performance---")
print("Student name:",name)
print("Total marks:",total)
print("Percentage",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)