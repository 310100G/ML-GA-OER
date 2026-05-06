import pandas as pd

original_file = "../../round_1/data_cleaning/data_cleaning.csv"     
ga_file = "../../round_1/exp_data/expr.xlsx"            
output_file = "data_cleaning.csv"    

df_original = pd.read_csv(original_file)
df_ga = pd.read_excel(ga_file)

original_columns = df_original.columns.tolist()
id_col = original_columns[0]  

if 'EXP_overpotential_10' in df_ga.columns:   
    if 'overpotential' in df_ga.columns:    
        df_ga['overpotential'] = df_ga['EXP_overpotential_10']       
    else:
        df_ga = df_ga.rename(columns={'EXP_overpotential_10': 'overpotential'})

df_ga[id_col] = None
df_ga = df_ga[[id_col] + [c for c in df_ga.columns if c != id_col]]

default_values = {
    'area': 1,
    'c_KOH': 1,
    'iR': 0.9,
    'cur_density': 10
}

for col in original_columns:
    if col not in df_ga.columns:
        if col in default_values:
            df_ga[col] = default_values[col]
        else:
            df_ga[col] = None  

df_ga = df_ga[original_columns]

df_merged = pd.concat([df_original, df_ga], axis=0).reset_index(drop=True)

df_merged.to_csv(output_file, index=False, encoding='utf-8-sig')

print("新合并文件已生成：", output_file)