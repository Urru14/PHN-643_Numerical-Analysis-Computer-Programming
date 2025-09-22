def bmi(weight, height):
    """Calculate BMI using the formula: weight / (height * height)"""
    return weight / (height * height)

def determine_obesity_grade(bmi):
    """Determine obesity grade based on the BMI value"""
    if 20 <= bmi <= 24.9:
        return "Grade 0 (desirable)"
    elif 25 <= bmi <= 29.9:
        return "Grade 1 (overweight)"
    elif 30 <= bmi <= 40:
        return "Grade 2 (obese)"
    elif bmi > 40:
        return "Grade 3 (morbidly obese)"
    else:
        return "Below desirable BMI range"


# Read weight and height from the user
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
    
# Calculate BMI
bmi1 = bmi(weight, height)
    
grade = determine_obesity_grade(bmi1)

print(f"Your BMI is: {bmi1:.2f}")
print(f"Obesity Grade: {grade}")

