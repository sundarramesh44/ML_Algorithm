import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plot

rf = pd.read_csv('Diabetes.csv')
single_column = ['Pregnancies','Glucose','Pressure','Skin','Insulin','BMI','Diabetes','Age']
features = rf[single_column]
outcome = rf['Outcome']

dtree = DecisionTreeClassifer()
dtree1 = dtree.fit(features,outcome)

tree.plot_tree(dtree1,feature_names = features)

data_input = pd.DataFrame([[6,148,72,35,0,33.6,0.627,50]]), columns = features)
output_data = dtree1.predict(data_input)

print(output_data)

