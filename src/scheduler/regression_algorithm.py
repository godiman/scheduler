
# Import libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import os


def reg_model(data):
    
    # Get the absolute data path
    data_path = os.path.abspath('data/wait_time.csv')
    # Load the dataset
    df = pd.read_csv(data_path)

    # View the dataset
    # print(df)
    
    # Data clceaning and preprocessing
    # Drop some columns in the dataset
    df.drop(['p1', 'p2', 'p3', 'p4', 'total_time_min', 'max_p', 'Unnamed: 0'], axis=1, inplace=True)
    # print(df)
    
    r_model = {}
    
    # Sum the total time a doctor spent with a patient
    total_min = df[['p1_minute', 'p2_minute', 'p3_minute', 'p4_minute']].sum(axis=1)
    # print(total_min)
    r_model['total_min'] = total_min
    
    # Building the model 
    reg_model = linear_model.LinearRegression()

    # Training the model
    reg_model.fit(df[['p1_minute', 'p2_minute', 'p3_minute', 'p4_minute']], df.avg_in_min)
    
    
    # The cofficient of the prediction
    # reg_model.coef_
    
    # The intercept of the prediction
    # reg_model.intercept_
    
    # Testing the model     
    avg_time = reg_model.predict([data])
    # view the average time
    # avg_time[0]
    
    r_model['avg_time'] = avg_time[0]
    
    return r_model
    
# data = [15,58,32,25]
# prediction = reg_model(data)
# print(prediction['total_min'], prediction['avg_time'])