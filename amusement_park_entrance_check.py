'''
You need to write a program that simulates an
amusement park entrance check.
Criteria:
● Age: Minimum 3 years old
● Height: Minimum 91.4 centimeters (36 inches)
● Accompaniment: Visitors under 12 must be with
an adult (18+)
Input:
● Ask the user for visitor's age (integer)
● Ask the user for visitor's height in
centimeters (float)
● Ask the user if the visitor under 12 is
accompanied by an adult (convert yes/no answer
to boolean)
Logic:
● Use if-elif-else statements to check eligibility
based on age, height, and accompaniment.
● Use boolean operators to combine conditions
(e.g., check if visitor is under 12).
Output:
● Print a welcome message if all criteria are met.
● Print specific messages for age or height
restrictions if not eligible.
● Print a message about accompaniment requirement
if the visitor is under 12 and not accompanied.
Bonus:
● Implement a ternary operator (optional) to
simplify the accompaniment check for visitors
under 12.
'''

age=int(input("Enter your age :"))
if age<3:
    print("Not Enter ,● Age: Minimum 3 years old ")

elif age<12 and age>=3:
    ask=str(input("is you accompanied by an adult? ")) 
    
    if ask=="yes" or ask =="YES":
        hight=float(input("Enter your hight : "))
        if hight >91.4:
            print("welcome to the park!")
        else:
            print("No ● Height: Minimum 91.4 centimeters (36 inches) ")
        
    elif ask=="no"or ask =="NO" :
        print("NOT GO cause dont have adult") 
        
        
elif age >=12:
    hight=float(input("Enter your hight : "))
    if hight >91.4:
        print("welcome to the park!")
    else:
        print("No ● Height: Minimum 91.4 centimeters (36 inches) ")
