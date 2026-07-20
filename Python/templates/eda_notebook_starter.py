# EDA Notebook Starter
# A minimal, reusable skeleton for exploratory data analysis.
# Copy into a .py file or paste cells into a Jupyter notebook.
# See: ../../Data_Wrangling/guides/data_exploration_ref.md

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()  # clean default theme

# 1. Load ---------------------------------------------------------------
df = pd.read_csv("data.csv")            # <- your data source

# 2. First look ---------------------------------------------------------
print(df.shape)
df.head()
df.info()
df.describe(include="all")

# 3. Missing data -------------------------------------------------------
print(df.isna().sum().sort_values(ascending=False))

# 4. Distributions ------------------------------------------------------
num_cols = df.select_dtypes("number").columns
df[num_cols].hist(figsize=(12, 8))
plt.tight_layout()

# 5. Relationships ------------------------------------------------------
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0)

# 6. Categorical breakdowns --------------------------------------------
for col in df.select_dtypes("object").columns[:5]:
    print(f"\n{col}:")
    print(df[col].value_counts().head())

# 7. Notes / hypotheses -------------------------------------------------
# - What stood out?
# - What needs cleaning (see data_cleaning_ref.md)?
# - What questions to test next (see Statistics/)?
