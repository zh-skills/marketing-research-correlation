# Marketing Research — Pearson Correlation Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python scripts for running Pearson correlation analysis on restaurant preference survey data.

## Files

| File | Description |
|------|-------------|
| `correlation-csv.py` | Correlates two preference columns (`Pref1` vs `Pref2`) from a CSV file |
| `correlation-xlsx.py` | Same analysis, reading from an Excel file (`Restaurant.xlsx`) |
| `correlation-xlsx5.py` | Runs all pairwise correlations across every numeric variable in `Restaurant5.xlsx` |
| `Restaurant.csv` / `Restaurant.xlsx` | Survey data used by the single-pair scripts |
| `Restaurant5.xlsx` | Survey data with multiple preference variables for the all-pairs analysis |

## Output

Each script prints the Pearson r statistic, p-value, and 95% confidence interval for each pair:

```
--- Pref1 vs Pref2 ---
Pearson r:   0.8321
P-value:     0.0003
95% CI:      (0.6104, 0.9401)
```

## Setup

```bash
pip install -r requirements.txt
```

Requirements: `pandas`, `scipy`, `openpyxl`

## Usage

```bash
# Single pair, CSV input
python correlation-csv.py

# Single pair, Excel input
python correlation-xlsx.py

# All pairwise combinations, Excel input
python correlation-xlsx5.py
```

> **Note:** `correlation-xlsx5.py` skips the first numeric column (respondent ID) before building pairs.

## License

This project is licensed under the [MIT License](LICENSE).
