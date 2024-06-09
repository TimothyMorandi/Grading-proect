"""The program to prompt the user to enter his marks where by
#score 70-100 is A
# score 60-69 B
# score 50-59 C
# 40-49 D
# score 0 -39 is FAil"""
Maths = int(input("Marks for Maths: "))
English = int(input("Marks for English: "))
Kiswahili = int(input("Marks for Swahili: "))
average =(Maths + English + Kiswahili) / 3
print(f"Your average is: {average} Marks")
if average >= 70:
    print("Your grade is: 'A' ")
elif average >= 60 and average == 69:
    print("Your grade is: 'B' ")
elif average >= 50 and average == 59:
    print("Your grade is: 'C'")
elif average >= 40 and average == 49:
    print("Your grade is: 'D'")
elif average <= 39:
    print("Your grade is: 'FAIL'")
else:
    print("You dint do your exams!")



