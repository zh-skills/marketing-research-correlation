import pandas as pd
from scipy import stats
data = pd.read_excel('Restaurant.xlsx')
x1 =data['Pref1']
x2 =data['Pref2']
results=stats.pearsonr(x1,x2)
print(f"Pearson r:   {results.statistic:.4f}")
print(f"P-value:     {results.pvalue:.4f}")
ci = results.confidence_interval()
print(f"95% CI:      ({ci.low:.4f}, {ci.high:.4f})")
