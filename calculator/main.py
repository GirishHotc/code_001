
import json
import numpy as np
import pandas as pd

file_name = open('E:\Python_coading\data.json')


def bmi_caculation(file_name):

    data = json.load(file_name)
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
    return (df)

def overweight_filter(df):
    temp = (df[(df.BMI >= 25) & (df.BMI <= 29.9)])
    return (len(temp))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bmi_df=bmi_caculation(file_name=file_name)
    overweight_count=overweight_filter(df=bmi_df)
    print('BMI DataFrame:')
    print(bmi_df)
    print('Overweight people Count:',overweight_count)


