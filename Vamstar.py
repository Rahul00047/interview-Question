import jsonify
import json
input_Json = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
# input_Json1 = jsonify(input_Json)
print(input_Json)
print("input_Json:",type(input_Json))
for x in input_Json:
    # print(x)
    height=x["HeightCm"]
    hm=height/100
    h1=hm*hm
    # print("h1:",h1)
    mass=x["WeightKg"]
    # print("mass:",mass)
    BMI=mass/h1
    # print("BMI:",BMI)
    x["BMI"]=BMI
    if (BMI <= 18.4):
        x["BMI Category"]="Underweight"
        x["Health risk"]="Malnutrition risk"
    elif (BMI >= 18.5 and BMI <= 24.9):
        x["BMI Category"] = "Normal weight"
        x["Health risk"] = "Low risk"
    elif (BMI >= 25 and BMI <= 29.9):
        x["BMI Category"] = "Overweight"
        x["Health risk"] = "Enhanced risk"
    elif (BMI >= 30 and BMI <= 34.9):
        x["BMI Category"] = "Moderately obese"
        x["Health risk"] = "Medium risk"
    elif (BMI >= 35 and BMI <= 39.9):
        x["BMI Category"] = "Severly obese"
        x["Health risk"] = "High risk"
    elif (BMI >= 40):
        x["BMI Category"] = "Very severly obese"
        x["Health risk"] = "Very high risk"
print("changed input_Json:", input_Json)
# h1 = height * heigh
# BMI = mass /h1t
