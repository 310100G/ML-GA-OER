import pandas as pd
import numpy as np
import time
from sklearn.model_selection import RepeatedKFold, GridSearchCV, cross_validate
from sklearn.metrics import make_scorer, mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor
import joblib


def tune_and_evaluate(model, param_grid, model_name, X, y, output_excel="model_comparison.xlsx"):

    print(f"\n 开始调参: {model_name}")
    start_time = time.time()

    cv_strategy = RepeatedKFold(n_splits=10, n_repeats=10, random_state=42)

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=cv_strategy,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        verbose=1
    )

    grid.fit(X, y)
    best_model = grid.best_estimator_
    best_params = grid.best_params_

    scoring = {
        "MAE": "neg_mean_absolute_error",
        "RMSE": "neg_root_mean_squared_error",
        "R2": "r2"
    }

    scores = cross_validate(best_model, X, y, cv=cv_strategy, scoring=scoring, n_jobs=-1)
    duration = time.time() - start_time

    results = {
        "Model": model_name,
        "Best_Params": str(best_params),
        "MAE_mean": -np.mean(scores["test_MAE"]),
        "MAE_std": np.std(scores["test_MAE"]),
        "RMSE_mean": -np.mean(scores["test_RMSE"]),
        "RMSE_std": np.std(scores["test_RMSE"]),
        "R2_mean": np.mean(scores["test_R2"]),
        "R2_std": np.std(scores["test_R2"]),
        "Time (s)": round(duration, 2)
    }

    print(f"{model_name} 完成，最佳参数: {best_params}")
    print(f"MAE: {results['MAE_mean']:.3f}, RMSE: {results['RMSE_mean']:.3f}, R²: {results['R2_mean']:.3f}")

    try:
        old_df = pd.read_excel(output_excel)
        new_df = pd.concat([old_df, pd.DataFrame([results])], ignore_index=True)
    except FileNotFoundError:
        new_df = pd.DataFrame([results])

    new_df.to_excel(output_excel, index=False)
    print(f"结果已保存至 {output_excel}")

    # joblib.dump(best_model, f"{model_name}_best_model.pkl")
    # print(f"💾 模型已保存: {model_name}_best_model.pkl\n")

    return results


if __name__ == "__main__":

    df = pd.read_csv("../data_cleaning/data_cleaning.csv")
    X = df.iloc[:, 1:-1].fillna(0)
    y = df.iloc[:, -1]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    models = {
        "GBR": (
            GradientBoostingRegressor(random_state=42),
            {
                "n_estimators": [50, 100, 150, 200, 250, 300],
                "learning_rate": [0.01, 0.03, 0.05, 0.07, 0.1],
                "max_depth": [5, 10, 15, 20, 25]
            }
        ),
        "XGB": (
            XGBRegressor(random_state=42, verbosity=0),
            {
                "n_estimators": [3, 5, 10, 20, 50],
                "learning_rate": [0.01, 0.1, 0.5],
                "subsample": [0.5, 0.8, 1.0],
                "max_depth": list(range(2, 10)),
                "min_child_weight": range(2,11,2),
                "gamma": [0, 0.1, 0.5],
                "colsample_bytree": [0.3, 0.5, 0.7, 1.0],
                "random_state": [1],
            }
        ),
        "RF": (
            RandomForestRegressor(random_state=42),
            {
                "n_estimators": [50, 100, 150, 200, 250, 300],
                "max_depth": [5, 10, 15, 20, 25]
            }
        )
    }

    all_results = []
    for name, (model, param_grid) in models.items():
        res = tune_and_evaluate(model, param_grid, model_name=name, X=X, y=y)
        all_results.append(res)

    summary_df = pd.DataFrame(all_results)
    summary_df = summary_df.sort_values(by="RMSE_mean")
    summary_df.to_excel("final_model_summary.xlsx", index=False)

    print("\n 所有模型已完成！最终汇总结果保存在 final_model_summary.xlsx")
    print(summary_df)
