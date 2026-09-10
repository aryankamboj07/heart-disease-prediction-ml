# # backend/train_model.py
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import joblib
# import os

# # Example: expect a CSV with columns matching features:
# # ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','target']
# DATA_CSV = "heart.csv"  # change to your dataset path

# if not os.path.exists(DATA_CSV):
#     raise FileNotFoundError(f"{DATA_CSV} not found. Put your dataset here or use your notebook to create model.pkl")

# df = pd.read_csv(DATA_CSV)
# X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang']]
# y = df['target']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# print("Train score:", model.score(X_train, y_train))
# print("Test score:", model.score(X_test, y_test))

# joblib.dump(model, "model.pkl")
# print("Saved model to model.pkl")




import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simple sample dataset (Heart Disease)
data = {
    "age":[52,54,63,44,55,60,50,41,62,58,57,45],
    "sex":[1,0,1,1,1,0,0,1,1,0,1,0],
    "cp":[0,1,2,1,2,1,0,1,1,0,1,2],
    "trestbps":[130,140,145,120,130,135,128,124,138,136,142,129],
    "chol":[250,260,240,200,220,230,210,190,260,250,240,220],
    "fbs":[0,0,0,1,0,0,1,0,0,0,0,0],
    "restecg":[1,0,1,1,0,1,0,1,1,0,1,1],
    "thalach":[160,155,150,170,180,175,165,172,158,159,160,161],
    "exang":[0,1,0,0,1,1,0,0,1,1,0,0],
    "target":[1,0,1,0,1,1,0,0,1,1,0,0]
}

df = pd.DataFrame(data)

X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang']]
y = df['target']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✔ model.pkl created successfully!")
