#QUESTION 1

#Taking 3 numbers as inputs
number1=float(input("Enter first number:-\n"))
number2=float(input("Enter second number:-\n"))
number3=float(input("Enter third number:-\n"))

average=(number1+number2+number3)/3    #Making formula for average
print("Average of the three numbers is:-\n",average)


#QUESTION 2

standard_deduction=10000
additional_dependent=3000
rate=0.02
gross_income=float(input("Enter your gross income in dollars\n"))
dependents=int(input("Enter number of dependents\n"))
taxable_income=gross_income-standard_deduction-(dependents*additional_dependent)
tax=taxable_income*rate
print("Your total tax:\n",tax)

#QUESTION3

student_list=[]
sid=int(input("Enter your student id:\n"))
name=str(input("Enter your name:\n"))
gender=str(input("Enter your gender(use M for male,F for female,U for unknown):\n"))
course_name=input("Enter your course name:\n")
cgpa=float(input("Enter your CGPA:\n"))
student_list.append(sid)
student_list.append(name)
student_list.append(gender)
student_list.append(course_name)
student_list.append(cgpa)
print(student_list)


#QUESTION 4

marks_list=[]
marks_1=float(input("Enter marks of first student:\n"))
marks_2=float(input("Enter marks of second student:\n"))
marks_3=float(input("Enter marks of third student:\n"))
marks_4=float(input("Enter marks of forth student:\n"))
marks_5=float(input("Enter marks of fifth student:\n"))
marks_list.append(marks_1)
marks_list.append(marks_2)
marks_list.append(marks_3)
marks_list.append(marks_4)
marks_list.append(marks_5)
marks_list.sort()
print(marks_list)


#QUESTION 5(a)

color_list=["Red","Green","White","Black","Pink","Yellow"]
color_list.pop(3)
print(color_list)

#QUESTION 5(b)

color_list=["Red","Green","White","Black","Pink","Yellow"]
color_list[3:5]=[];color_list.insert(3,"Purple")
print(color_list)
