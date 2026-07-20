# Data Cleaning Template
# A reusable checklist-as-code for turning raw data into analysis-ready data.
# Follow alongside: ../guides/data_cleaning_ref.md

import pandas as pd

df = pd.read_csv("raw_data.csv")
df = df.copy()                          # never mutate the original

# 1. Inspect ------------------------------------------------------------
print(df.shape)
df.info()

# 2. Standardize column names ------------------------------------------
df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))

# 3. Fix data types -----------------------------------------------------
# df["date"] = pd.to_datetime(df["date"])
# df["price"] = df["price"].astype(float)

# 4. Trim/clean text ----------------------------------------------------
for col in df.select_dtypes("object").columns:
    df[col] = df[col].str.strip()

# 5. Missing data -------------------------------------------------------
print(df.isna().sum())
# df = df.dropna(subset=["key_col"])           # drop where essential
# df["num"] = df["num"].fillna(df["num"].median())

# 6. Duplicates ---------------------------------------------------------
before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df)} duplicate rows")

# 7. Standardize categories --------------------------------------------
# df["state"] = df["state"].str.title().replace({"Ny": "New York"})

# 8. Outliers (IQR flag) ------------------------------------------------
# q1, q3 = df["num"].quantile([.25, .75]); iqr = q3 - q1
# df["is_outlier"] = (df["num"] < q1 - 1.5*iqr) | (df["num"] > q3 + 1.5*iqr)

# 9. Save cleaned -------------------------------------------------------
df.to_csv("clean_data.csv", index=False)
print("Saved clean_data.csv")
