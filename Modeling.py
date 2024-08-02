import pandas as pd 
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.read_csv("./Data for Machine Learning_final.csv")

df = df.dropna()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


X = df.drop(columns=['price']).to_numpy()
y = df['price'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.17, random_state=0 )

model = RandomForestRegressor(n_estimators=400, max_depth=20, random_state=0)
model.fit(X_train, y_train.ravel())  # Flatten y_train to 1D array

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_mae = mean_absolute_error(y_train, train_predictions)
test_mae = mean_absolute_error(y_test, test_predictions)

train_r2 = r2_score(y_train, train_predictions)
test_r2 = r2_score(y_test, test_predictions)

print("Training Mean Absolute Error (MAE):", train_mae)
print("Testing Mean Absolute Error (MAE):", test_mae)
print("Training R2 Score:", train_r2)
print("Testing R2 Score:", test_r2)

joblib.dump(model, "Random_Forest_model.joblib", compress=3)  # Save the model using joblib
print("Model saved successfully!")