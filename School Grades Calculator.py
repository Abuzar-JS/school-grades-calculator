# In this program we are creating an application to calculate student percentage and provides him grades accordingly with If-Else statement
# Program by Muhammad Abuzar Jamshaid
# https://github.com/Abuzar-JS/school-grades-calculator

obtained_marks= eval(input("Enter obtained marks: ")) #User Will Enter it's Obtained Marks
t_marks=eval(input("Enter total marks: ")) #Enter Total Marks
marks = (int(obtained_marks*100/t_marks)) # We applied mathematics formula to Calculate percentage
print("Your Got ",marks,"%")

if marks > 100: # If user enter wrong values such as Greater obtained marks out of total marks then following message wil print
    print("Obtained marks are Greater than Total marks")
    print("Please Re-Enter Values to Calculate percentage")
elif marks >= 90: # If user got greater than or equal to 90% the following message will print
    print("Grade: A")
    print("Excellent")
elif marks >= 80: # If user got greater than or equal to 80% the following message will print
    print("Grade: B")
    print("Good Job")
elif marks >= 70: # If user got greater than or equal to 70% the following message will print
    print("Grade: C")
    print("Good Work")
elif marks >= 60: # If user got greater than or equal to 60% the following message will print
    print("Grade: D")
    print("Keep Working Hard")
elif marks >= 50: # If user got greater than or equal to 50% the following message will print
    print("Grade: F")
    print("Hard Work Next time")
else: # If user got less than 50% marks then following message will print
    print("You can still improve. Work hard next time ")

