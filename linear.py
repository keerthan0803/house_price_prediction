import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv(r'C:\Users\keert\Downloads\House_Price_Dataset_Linear.csv')
del df['Id']  # Remove the Id column

# Encode categorical columns
label_encoders = {}
categorical_columns = ['Location', 'Condition', 'Garage']
for col in categorical_columns:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Save the model and label encoders as a pickle file for use with the backend
model_data = {
    'model': model,
    'label_encoders': label_encoders,
    'feature_names': df.columns[:-1].tolist()
}
with open('model.pkl', 'wb') as f:
    pickle.dump(model_data, f)
print("Model saved as model.pkl")
print("Feature names:", model_data['feature_names'])
