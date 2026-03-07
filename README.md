# Laptop Price Predictor

This project predicts laptop prices based on hardware specifications and brand-related features using Machine Learning models.

---

## Project Overview

The dataset contains 1303 laptops with features such as:

- Company  
- TypeName  
- Operating System  
- CPU Brand  
- GPU Brand  
- RAM  
- SSD / HDD  
- Screen Size  
- Resolution  
- Touchscreen / IPS  
- Weight  
- Price (target variable)

The goal is to predict `Price_euros` from these features.

---

## Models Implemented

We built and evaluated **two regression models**:

---

### 1. Linear Regression (Log-Transformed Target)

**Approach:**
- Applied `log(Price_euros)` during training.
- Predicted in log space.
- Used `exp()` to convert predictions back to real price.

**Why log transform?**
- Price distribution is heavily skewed.
- Log transformation stabilizes variance.
- Reduces extreme prediction errors.
- Prevents negative price outputs.

**Post-processing:**
- A minimum boundary (e.g., €100 or dataset minimum €174) is applied to prevent unrealistic low predictions.

**Strengths:**
- Simple and interpretable.
- Handles skewed price distribution well.
- More stable for extreme low-end specs.

**Limitations:**
- May underperform on highly nonlinear relationships.
- Less accurate for very complex feature interactions.

---

### 2. Random Forest Regressor

**Approach:**
- Trained directly on real price values.
- Used tuned parameters:
  - `n_estimators`
  - `max_depth`
  - `min_samples_leaf`

**Why Random Forest?**
- Captures nonlinear relationships.
- Handles categorical one-hot features well.
- Robust to noise and feature interactions.

**Strengths:**
- Better performance on typical mid-range laptops.
- Handles complex patterns automatically.

**Limitations:**
- Poor extrapolation on rare/low-frequency specs.
- Biased toward dense price regions in dataset.
- Can predict unrealistically high prices for rare combinations.

---

## Dataset Price Distribution

- Minimum: €174  
- 25th percentile: €599  
- Median: €977  
- 75th percentile: €1487  
- Maximum: €6099  

Most laptops fall between €600–€1500, making extreme low-end predictions difficult without log transformation.

---

## Preprocessing Steps

- Merged low-frequency companies into `"Others"`.
- Merged OS variants:
  - Windows 10 + Windows 10 S
  - macOS + Mac OS X
- Applied One-Hot Encoding (without dropping first column).
- Calculated `ppi` (pixels per inch) from resolution and screen size.
- Saved `model_columns.pkl` to ensure feature consistency during prediction.

---

