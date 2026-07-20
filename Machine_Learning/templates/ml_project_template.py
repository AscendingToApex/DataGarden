# ML Project Template (scikit-learn)
# A minimal end-to-end supervised-learning skeleton.
# Follow alongside: ../guides/ml_project_checklist_ref.md
#                   ../guides/ml_data_prep_ref.md
#                   ../guides/ml_model_evaluation_ref.md

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Load & split -------------------------------------------------------
df = pd.read_csv("data.csv")
TARGET = "target"                       # <- your label column
X = df.drop(columns=[TARGET])
y = df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 2. Preprocess (fit on train only -> no leakage) -----------------------
num_cols = X.select_dtypes("number").columns
cat_cols = X.select_dtypes("object").columns

pre = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]), num_cols),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
])

# 3. Model in a pipeline ------------------------------------------------
pipe = Pipeline([("pre", pre),
                 ("model", RandomForestClassifier(random_state=42))])

# 4. Tune with cross-validation ----------------------------------------
grid = GridSearchCV(pipe, {"model__n_estimators": [100, 300],
                           "model__max_depth": [None, 10]},
                    cv=5, scoring="f1_weighted")
grid.fit(X_train, y_train)
print("Best params:", grid.best_params_)

# 5. Evaluate on the held-out test set ----------------------------------
y_pred = grid.predict(X_test)
print(classification_report(y_test, y_pred))
