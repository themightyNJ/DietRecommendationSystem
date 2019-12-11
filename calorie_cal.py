print("BMI Calculator....")
gender = input("Enter your Gender (Male(M) or Female(F)): ")
weight = float(input("Enter Weight in Kilograms : "))
height = float(input("Enter Height in Meters : "))
age = int(input("Enter your age : "))

BMI = weight / height**2
print(BMI)

if BMI <= 18.5 :
    print("You are Underweight")
elif BMI >= 18.5 and BMI <= 24.9 :
    print("You have Normal Weight")
elif BMI >= 25 and BMI <= 29.9 :
    print("You are Overweighted")
else :
    print("You have Obesity, please maintain your diet")

print("""Types of LIFESTYLE :
1.Sedentary Lifestyle - Light or no exercise.
2.Lightly Active Lifestyle - Light exercise or sports 1-3 days/week.
3.Moderate Active Lifestyle - Moderate exercise or sports 3-5 days/week.
4.Very Active Lifestyle - Hard exercise or sports 6-7 days/week.
5.Extra Active Lifestyle - Very hard exercise or sports  6-7 days/week.""")

activity_type = int(input(("Enter your Activity Type (1,2...,5) : ")))

if activity_type == 1 :
    calory_constant = 1.3
elif activity_type == 2 :
    calory_constant = 1.55
elif activity_type == 3 :
    calory_constant = 1.65
elif activity_type == 4 :
    calory_constant = 1.80
else :
    calory_constant = 2.00

if gender == "male" or gender == "m":
    BMR = (10*weight) + (6.25*height*100) - (5*age) + 5
    print("Your BMR is : ", BMR)
    calories = BMR*calory_constant
    print(calories, "Calories needed per day")
else :
    BMR = (10*weight) + (6.25*height*100) + (5*age) - 161
    print("Your BMR is : ", BMR)
    calories = BMR*calory_constant
    print(calories, "Calories needed per day")
