"""
Created on Thu Jun 17 21:54:11 2021
@author: daniel
"""

print('###################################################')
print('                   BMI Calculator                  ')
print('###################################################')
print()
print("This program can't substitute any doctor or health professional diagnosis")
print('BMI may not be precise for everyone!')

weight = float(input('Insert your weight (kg)'))
height = float(input('Insert your height (meters)'))
print()

bmi = round(weight / (height ** 2), 2)

print('Your BMI is {}'.format(bmi))

if bmi < 18.5:
    print('Underweight')
elif 18.6 <= bmi and bmi < 24.9:
    print('Normal weight')
elif 25 <= bmi and bmi < 29.9:
    print('Overweight')
elif 30 <= bmi and bmi < 34.9:
    print('Obese')
elif 35 <= bmi and bmi < 39.9:
    print('Obese (severe)')
else:
    print('Obese (morbid)')