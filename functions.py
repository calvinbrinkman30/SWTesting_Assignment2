def LbsToKgs(p):
    return round(p*0.45, 3)

def HeightToMeters(f, i):
    i += f*12
    return round(i*0.025, 3)

def BMI(k, m):
    return round(k/(m**2), 3)

def Categorize(bmi):
    if bmi < 18.4:
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"
    return "obese"

def getHeight():
    try:
        f, i = input().split(", ")
        f = float(f)
        i = float(i)
    except:
        print("Please enter a valid integer combination")
        f, i = getHeight()
    if (f%1) != 0:
        print("Please enter a valid integer combination")
        f, i = getHeight()
    if (i%1) != 0:
        print("Please enter a valid integer combination")
        f, i = getHeight()
    return int(f), int(i)

def getWeight():
    try:
        p = float(input())
    except:
        print("Please enter a valid number")
        p = getWeight()
    return p