import functions as func
    
print("Enter your height as: feet, inches")
f, i = func.getHeight()
print("Enter your weight in pounds: ")
p = func.getWeight()

k = func.LbsToKgs(p)
m = func.HeightToMeters(f, i)
bmi = func.BMI(k, m)
print("---------------------------------")
print(f'With a height of {f}\' {i}\" and a weight of {p} lbs')
print(f'Your BMI is {bmi}, and you are categorized as {func.Categorize(bmi)}')