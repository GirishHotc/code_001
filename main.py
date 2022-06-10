# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import numpy as np
import pandas as pd


def print_hi(name):
    # Opening JSON file
    f = open('E:\Python_coading\data.json')
    data = json.load(f)
    df = pd.DataFrame.from_dict(data)
    new_df = list()
    new_df.clear()
    for i in range(len(df)):
        new_df.append(round(df['WeightKg'][i] / (((df['HeightCm'][i] * df['HeightCm'][i]) / 10000)), 1))
    df['BMI'] = new_df
    new_mic = list()
    new_hr = list()
    new_mic.clear()
    new_hr.clear()

    for i in range(len(new_df)):
        if new_df[i] <= 18.4:
            new_mic.append('Underweight')
            new_hr.append('Malnutrition risk')
        elif 18.4 < new_df[i] <= 24.9:
            new_mic.append('Normal Weight')
            new_hr.append('Low risk')
        elif 24.9 < new_df[i] <= 29.9:
            new_mic.append('OverWeight')
            new_hr.append('Enhanced risk')
        elif 29.9 < new_df[i] <= 34.9:
            new_mic.append('Moderately obese')
            new_hr.append('Medium risk')
        elif 34.9 < new_df[i] <= 39.9:
            new_mic.append('Severely obese')
            new_hr.append('High risk')
        elif new_df[i] > 39.9:
            new_mic.append('Very severely obese ')
            new_hr.append('Very high risk')

    df['BMI_Category'] = new_mic
    df['Health_Risk'] = new_hr
    print(df)

    # Task 2
    temp = (df[(df.BMI >= 25) & (df.BMI <= 29.9)])
    print("No of overweight people ", len(temp))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
