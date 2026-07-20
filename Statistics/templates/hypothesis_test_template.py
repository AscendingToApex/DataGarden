# Hypothesis Test Template
# A reusable skeleton for a two-sample comparison.
# Follow alongside: ../guides/hypothesis_testing_ref.md
#                   ../guides/ab_testing_ref.md

import numpy as np
from scipy import stats

# 1. State hypotheses ---------------------------------------------------
# H0: the two group means are equal
# H1: the two group means differ (two-tailed)
ALPHA = 0.05

# 2. Data ---------------------------------------------------------------
group_a = np.array([...])   # control
group_b = np.array([...])   # variant

# 3. Check assumptions (normality, equal variance) ----------------------
print("Normality A:", stats.shapiro(group_a))
print("Normality B:", stats.shapiro(group_b))
equal_var = stats.levene(group_a, group_b).pvalue > 0.05

# 4. Choose & run the test ---------------------------------------------
# Welch's t-test (equal_var=False) is the safe default for unequal variances.
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=equal_var)

# 5. Report -------------------------------------------------------------
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")
if p_value <= ALPHA:
    print("Reject H0 — the difference is statistically significant.")
else:
    print("Fail to reject H0 — no significant difference detected.")

# 6. Effect size (Cohen's d) — always report alongside the p-value ------
pooled_sd = np.sqrt((group_a.var(ddof=1) + group_b.var(ddof=1)) / 2)
cohens_d = (group_a.mean() - group_b.mean()) / pooled_sd
print(f"Cohen's d = {cohens_d:.3f}")
