import json
import pandas as pd
import logging
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)


def _get_bmi_df(json_data: dict):
    """
    Return dataframe with additional columns BMI, health risk , BMI Category
    Args:
        json_data: data in json format
    Returns:
        df_health: with additional columns BMI, health risk , BMI Category
    """
    try:
        df_health = pd.DataFrame.from_dict(json_data)
        bmi_list = list()
        bmi_category_list = list()
        high_risk_list = list()
        bmi_category_list.clear()
        high_risk_list.clear()
        bmi_list.clear()
        for i in range(len(df_health)):
            bmi_list.append(round(df_health['WeightKg'][i] /
                                  (((df_health['HeightCm'][i] * df_health['HeightCm'][i]) / 10000)), 1))
        df_health['BMI'] = bmi_list

        for i in range(len(bmi_list)):
            if bmi_list[i] <= 18.4:
                bmi_category_list.append('Underweight')
                high_risk_list.append('Malnutrition risk')
            elif 18.4 < bmi_list[i] <= 24.9:
                bmi_category_list.append('Normal Weight')
                high_risk_list.append('Low risk')
            elif 24.9 < bmi_list[i] <= 29.9:
                bmi_category_list.append('OverWeight')
                high_risk_list.append('Enhanced risk')
            elif 29.9 < bmi_list[i] <= 34.9:
                bmi_category_list.append('Moderately obese')
                high_risk_list.append('Medium risk')
            elif 34.9 < bmi_list[i] <= 39.9:
                bmi_category_list.append('Severely obese')
                high_risk_list.append('High risk')
            elif bmi_list[i] > 39.9:
                bmi_category_list.append('Very severely obese ')
                high_risk_list.append('Very high risk')

        df_health['BMI_Category'] = bmi_category_list
        df_health['Health_Risk'] = high_risk_list
        return df_health

    except Exception as e:
        logger.error(e)


def _get_overweight_count(df: pd.DataFrame):
    """
    Return COUNT of overweight people
    Args:
        df: dataframe with BMI details
    Returns:
        count of overweight people
    """
    try:
        temp = (df[(df.BMI >= 25) & (df.BMI <= 29.9)])
        return len(temp)

    except Exception as e:
        logger.error(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_data = open('../data/data.json')
    json_data = json.load(file_data)
    bmi_Df = _get_bmi_df(json_data=json_data)
    print(bmi_Df)
    overweight_count = _get_overweight_count(df=bmi_Df)
    print("Total Number of Overweight People :", overweight_count)
