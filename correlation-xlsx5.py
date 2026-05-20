import pandas as pd
from scipy import stats
from itertools import combinations

data = pd.read_excel('Restaurant5.xlsx')
# [1:] slices off the first numeric column before building the pairs
# The first column is the respondent ID, which is not a variable we want to correlate
cols = data.select_dtypes(include='number').columns.tolist()[1:]

for col1, col2 in combinations(cols, 2):
    results = stats.pearsonr(data[col1], data[col2])
    ci = results.confidence_interval()
    print(f"--- {col1} vs {col2} ---")
    print(f"Pearson r:   {results.statistic:.4f}")
    print(f"P-value:     {results.pvalue:.4f}")
    print(f"95% CI:      ({ci.low:.4f}, {ci.high:.4f})")
    print()
