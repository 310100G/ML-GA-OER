import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge, Ridge
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler

df_path = '../data_cleaning/data_cleaning.csv'
df = pd.read_csv(df_path)

drop_cols = ["ID", "overpotential"]
X = df.drop(columns=drop_cols)
X = X.fillna(0)
y = df["overpotential"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

models = {
    "RandomForest": RandomForestRegressor(random_state=0),
    "SVR": SVR(),
    "GBR": GradientBoostingRegressor(random_state=0),
    "XGB": XGBRegressor(random_state=0, verbosity=0),
    "BayesianRidge": BayesianRidge(),
    "Ridge": Ridge()
}

rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=42)

def evaluate_model_cv(model, X, y, rkf):
    mae_scores, rmse_scores, r2_scores = [], [], []
    
    for train_idx, test_idx in rkf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        mae_scores.append(mean_absolute_error(y_test, y_pred))
        rmse_scores.append(mean_squared_error(y_test, y_pred, squared=False))
        r2_scores.append(r2_score(y_test, y_pred))
    
    return {
        "MAE": np.mean(mae_scores),
        "RMSE": np.mean(rmse_scores),
        "R2": np.mean(r2_scores)
    }

results = []

for name, model in models.items():
    print(f"正在训练模型：{name} ...")
    scores = evaluate_model_cv(model, X, y, rkf)
    scores["Model"] = name
    results.append(scores)

results_df = pd.DataFrame(results)[["Model", "MAE", "RMSE", "R2"]]
results_df = results_df.sort_values(by="RMSE")

results_df.to_excel("model_comparison.xlsx", index=False)

print("model_comparison.xlsx")
print(results_df)
