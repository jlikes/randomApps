import math
#variables
activity = 0
gender = 0
weight = 0
height = 0
age = 0
bmr = 0

#setter functions
def setGender():
    global gender
    while True:
        print('\nAre you a (1) male or a (2) female?')
        gender = input()
        print(gender)
        if(gender == '1'):
            break
        if(gender == '2'):
            break
    return gender

def setWeight():
    print('\nHow much do you weigh? (in lbs)')
    weight = input()
    return float(weight) * .453592

def setHeight():
    print('\nHow tall are you? (in inches)')
    height = input()
    return float(height) * 2.54

def setAge():
    print('\nHow old are you?')
    age = input()
    return age

def setActivityLevel():
    print('\nSelect an activity level: ')
    print('1) Sedentary (Little or no Exercise)')
    print('2) Lightly Active (Light exercise 1-3 days / week)')
    print('3) Moderately Active (Moderate exercise 3-5 days / week)')
    print('4) Very Active (Hard exercise 6-7 days / week)')
    print('5) Extra Active (Very hard exercise / physical job or 2x training')
    activity = input()
    return activity

def calToMaintain():
    if activity == '1':
        print('Calories to maintain = ', int(bmr*1.2))
    if activity == '2':
        print('Calories to maintain = ', int(bmr*1.375))
    if activity == '3':
        print('Calories to maintain = ', int(bmr*1.55))
    if activity == '4':
        print('Calories to maintain = ', int(bmr*1.725))
    if activity == '5':
        print('Calories to maintain = ', int(bmr*1.9))

def calToGain():
    if activity == '1':
        print('Calories to gain = ', int(bmr*1.2+500))
    if activity == '2':
        print('Calories to gain = ', int(bmr*1.375+500))
    if activity == '3':
        print('Calories to gain = ', int(bmr*1.55+500))
    if activity == '4':
        print('Calories to gain = ', int(bmr*1.725+500))
    if activity == '5':
        print('Calories to gain = ', int(bmr*1.9+500))

def calToLose():
    if activity == '1':
        print('Calories to lose = ', int(bmr*1.2-500))
    if activity == '2':
        print('Calories to lose = ', int(bmr*1.375-500))
    if activity == '3':
        print('Calories to lose = ', int(bmr*1.55-500))
    if activity == '4':
        print('Calories to lose = ', int(bmr*1.725-500))
    if activity == '5':
        print('Calories to maintain = ', int(bmr*1.9-500))

def calcBmr():
    if gender == '1':
        bmr = 66.47 + (13.7 * float(weight)) + (5 * float(height)) - (6.8 * float(age))
        return bmr
    elif gender == '2':
        bmr = 655.1 + (9.6 *  float(weight)) + (1.8 * float(height)) - (4.7 * float(age))
        return bmr

#program begins here
gender = setGender()
weight = setWeight()
height = setHeight()
age = setAge()
activity = setActivityLevel()
bmr = calcBmr()
print()
calToLose()
calToMaintain()
calToGain()


#debug
##print(gender)
##print(weight)
##print(height)
##print(age)
##print(activity)
##print(int(bmr))
