import pandas as pd
import numpy as np

def clean_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    df_cleaned = pd.DataFrame()

    df_cleaned['ID'] = df_raw['参考文献']

    substrate_map = {'镍': 28, '铁': 26, '铜': 29, '碳': 6}
    df_cleaned['substrate'] = df_raw['基底'].map(substrate_map).fillna(28)

    method_map = {'恒电流': 1, '恒电位': 2, '循环伏安': 3}
    df_cleaned['method'] = df_raw['沉积方法'].map(method_map).fillna(2)

    column_map = {
        '沉积电流A/cm2': 'GCI',
        '沉积电压': 'CPV',
        '沉积电压+': 'CV+',
        '沉积电压-': 'CV-'
    }
    for raw_col, new_col in column_map.items():
        if raw_col in df_raw.columns:
            df_cleaned[new_col] = df_raw[raw_col]
        else:
            df_cleaned[new_col] = np.nan

    df_cleaned['area'] = df_raw['沉积面积cm2'].fillna(1)
    df_cleaned['time'] = df_raw['沉积时间/s']
    df_cleaned['Fe_valence'] = df_raw['铁价态']

    df_cleaned['Ni'] = df_raw['浓度M.1'].fillna(0)
    df_cleaned['Fe'] = df_raw['浓度M'].fillna(0)

    dopant_z_map = {'S': 16, 'P': 15, 'Co': 27, 'W': 74, 'Mo': 42, 'Sn': 50, 'Cr': 24, 'Mn': 25}
    dopant_Z = []
    dopant_conc = []
    for i in range(len(df_raw)):
        dopant = df_raw.loc[i, '掺杂元素1']
        if pd.notnull(dopant) and str(dopant).strip() in dopant_z_map:
            dopant_Z.append(dopant_z_map[str(dopant).strip()])
            conc = df_raw.loc[i, '浓度']
            dopant_conc.append(conc if pd.notnull(conc) else np.nan)
        else:
            dopant_Z.append(pd.NA)
            dopant_conc.append(np.nan)

    df_cleaned['dopant_Z'] = dopant_Z
    df_cleaned['dopant_conc'] = dopant_conc

    df_cleaned['pH'] = df_raw['PH']
    if df_raw['电解质浓度KOH/M'].nunique() <= 2:
        c_KOH_map = {1: 1, 0.3: 6}
        df_cleaned['c_KOH'] = df_raw['电解质浓度KOH/M'].map(c_KOH_map)
    else:
        df_cleaned['c_KOH'] = df_raw['电解质浓度KOH/M']

    df_cleaned['iR'] = df_raw['iR矫正'].fillna(0.9)
    df_cleaned['cur_density'] = df_raw['电流密度ma/cm2'].fillna(10)

    df_cleaned['overpotential'] = df_raw['过电位mv']

    print("清洗后缺失值统计：")
    print(df_cleaned.isnull().sum())

    return df_cleaned

df_raw = pd.read_excel("原始数据.xlsx")
print(df_raw.head())
print(df_raw.columns.tolist())


df_cleaned = clean_data(df_raw)

df_cleaned.to_csv("data_cleaning.csv", index=False)

print(df_cleaned.head())


