import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import joblib

# music_data=pd.read_csv('music.csv')
# X=music_data.drop(columns=['genre'])
# y=music_data['genre']
# # X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.8)

# model=DecisionTreeClassifier()
# model.fit(X,y)
model=joblib.load('music-recommender.joblib')

predictions=model.predict([[21,1],[22,0]])
print(predictions)
# score= accuracy_score(y_test,predictions)
# print(score)