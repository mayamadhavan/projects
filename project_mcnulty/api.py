import numpy as np
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


pipeline = pickle.load(open('./model/model.pkl', 'rb'))
columns = pickle.load(open('./model/columns.pkl', 'rb'))
city_df_dict= pickle.load(open('./model/city_df_dict.pkl', 'rb'))
replacements= pickle.load(open('./model/replacements.pkl', 'rb'))

example = {
  'class_of_admission': 'H-1B',
  'country_of_citizenship': 'INDIA',
  'employer_state': 'NJ',
  'foreign_worker_info_city': 'san jose',
  'foreign_worker_info_education': 'High School',
  'job_category': 'Other'
}

def prediction(features):
    print(features)
    try:
        city_origin=replacements[features['foreign_worker_info_city'].upper()]
    except:
        city_origin=features['foreign_worker_info_city'].upper()
    try:
        city_pop=city_df_dict['pop'][city_origin]
    except:
        city_pop=300.000

    test_case = pd.DataFrame({'class_of_admission': features['class_of_admission'],
                      'country_of_citizenship': features['country_of_citizenship'],
                      'employer_state': features['employer_state'],
                      'foreign_worker_info_city': city_pop,
                      'foreign_worker_info_education': features['foreign_worker_info_education'],
                      'job_category': features['job_category']}, index=[0])

    test_case_dummies=pd.get_dummies(test_case)
    missing_cols=set(columns) - set(test_case_dummies.columns)
    for c in missing_cols:
        test_case_dummies[c] = 0
    test_case_dummies = test_case_dummies[columns]


    prob_certified = pipeline.predict_proba(test_case_dummies)[0, 1]
    outcome=''
    if int(prob_certified > 0.5):
        outcome+='Denied Visa'
    else:
        outcome+='Certified Visa'
    result = {
        'prediction': outcome,
        'prob_certified': round(prob_certified*100, 0)
    }
    return result

if __name__ == '__main__':
    print(prediction(example))
