import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

def save_model_results(model_name, best_params, y_train, y_pred_train, y_test, y_pred_test, output_file="model_results.xlsx"):
    metrics = {
        "Model": model_name,
        "Best_Params": str(best_params),
        "train_MAE": mean_absolute_error(y_train, y_pred_train),
        "train_RMSE": np.sqrt(mean_squared_error(y_train, y_pred_train)),
        "train_R2": r2_score(y_train, y_pred_train),
        "test_MAE": mean_absolute_error(y_test, y_pred_test),
        "test_RMSE": np.sqrt(mean_squared_error(y_test, y_pred_test)),
        "test_R2": r2_score(y_test, y_pred_test),
    }
    metrics_df = pd.DataFrame([metrics])

    train_results = pd.DataFrame({
        "Set": "Train",
        "True": y_train,
        "Pred": y_pred_train
    })
    test_results = pd.DataFrame({
        "Set": "Test",
        "True": y_test,
        "Pred": y_pred_test
    })
    pred_results = pd.concat([train_results, test_results], ignore_index=True)

    if not os.path.exists(output_file):  
        
        with pd.ExcelWriter(output_file, engine="openpyxl", mode="w") as writer:
            metrics_df.to_excel(writer, sheet_name="Metrics", index=False)
            pred_results.to_excel(writer, sheet_name=f"{model_name}_Pred", index=False)
    else:  
        
        with pd.ExcelWriter(output_file, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            
            metrics_df.to_excel(writer, sheet_name="Metrics", index=False, header=False,
                                startrow=writer.sheets["Metrics"].max_row)
            
            pred_results.to_excel(writer, sheet_name=f"{model_name}_Pred", index=False)

    print(f"{model_name} 的结果已保存到 {output_file}")