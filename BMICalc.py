# Choose the type of measurment
measurment = input("Hello, and welcome to Jackson's Body Mass Index calculator. Do you prefer Metric or Imperial units? Choose 1 for Metric or 2 for Imperial. ")
measurment_integer = int(measurment)

# Metric Units
if measurment_integer == 1:
    #Meters or centimeters
    Met_Unit = input("Cool. Would you like your height to be in centimeters or meters? Choose 1 for centimeters or 2 for meters." )
    Met_Unit_Integer = int(Met_Unit)

    # Centimeters
    if Met_Unit_Integer == 1:
        height_Met_cm = input("That's great. What is your height in centimeters? ")
        weight_Met = input("What is your weight in kilograms? ")
        weight_integer_Met = float(weight_Met)
        height_integer_Met_cm = float(height_Met_cm)
        BMI = weight_integer_Met/(height_integer_Met_cm**2)*10000

    # Meters
    if Met_Unit_Integer == 2:
        height_Met_m = input("That's cool. What's your height in meters? ")
        weight_Met = input("What is your weight in kilograms? ")
        weight_integer_Met = float(weight_Met)
        height_integer_Met_m = float(height_Met_m)
        BMI = weight_integer_Met/(height_integer_Met_m**2)

# Imperial Units
if measurment_integer == 2:
    weight_Imp = input("What is your weight in pounds? ")
    height_Imp = input("That's great. Whats your height in inches? ")
    weight_integer_Imp = float(weight_Imp)
    height_integer_Imp = float(height_Imp)
    BMI = weight_integer_Imp/(height_integer_Imp**2)*703

# Mapping your BMI
BMI_S = str(BMI)
print("Your BMI is " + BMI_S)
if BMI <18.5:
    print("You are underweight")
if BMI >18.5 and BMI <25:
    print("You are normal")
if BMI >25 and BMI <30:
    print("You are overweight")
if BMI >30 and BMI <40:
    print("You are obese")
if BMI >40:
    print("You are morbidly obese")
