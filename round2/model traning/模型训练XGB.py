import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from xgboost import XGBRegressor
from utils import save_model_results
from sklearn.preprocessing import StandardScaler
import joblib
import os

df_path = '../data_cleaning/data_cleaning.csv'
df = pd.read_csv(df_path)

X = df.iloc[:, 1:-1]
X = X.fillna(0)
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

param_grid = {
    "n_estimators": [3, 5, 10, 20, 30, 40],
    "learning_rate": [0.01, 0.1, 0.5],
    "subsample": [0.5, 0.8, 1.0],   
    "min_child_weight": range(2,11,2),
    "gamma": [0, 0.1, 0.5],
    "colsample_bytree": [0.3, 0.5, 0.7, 1.0],
    "random_state": [1],
}


cv_strategy = KFold(n_splits=10, shuffle=True, random_state=42)

xgb = XGBRegressor(random_state=42)
grid = GridSearchCV(xgb, param_grid, cv=cv_strategy, scoring="neg_mean_squared_error", n_jobs=-1)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

y_pred_train = best_model.predict(X_train)
y_pred_test = best_model.predict(X_test)

save_model_results(
    model_name="XGB",
    best_params=grid.best_params_,
    y_train=y_train, y_pred_train=y_pred_train,
    y_test=y_test, y_pred_test=y_pred_test,
    output_file="model_results.xlsx")

model_filename = "xgb_model.pkl"
joblib.dump(best_model, model_filename)


scaler_filename = "standard_scaler.pkl"
joblib.dump(scaler, scaler_filename)


