import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# read the data from the CSV file into a pandas DataFrame
data = pd.read_csv('Salary_Data.csv')

# split the data into input (years of experience) and output (salary) variables
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

# create a linear regression model
model = LinearRegression()

# fit the model to the data
model.fit(X, y)

# create a pickle file of the trained model
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
    
