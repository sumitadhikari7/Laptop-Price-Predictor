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

## ⚠️ Model Limitations Observed

During experimentation, two regression models were evaluated: **Linear Regression** and **Random Forest Regressor**.

### Linear Regression
The linear model was trained using a log-transformed target variable (`log(price)`) to address the skewed distribution of laptop prices.  
However, during prediction the model occasionally produced **extreme values** when encountering feature combinations outside the range of the training data.

This occurs because:
- Linear Regression extrapolates beyond the training distribution.
- Small deviations in log-space can lead to **very large values after exponential transformation**.

As a result, the linear model was not suitable for deployment.

### Random Forest
Random Forest performed more reliably overall, achieving an **R² score of ~0.81** on the test set.

However, another limitation was observed:
- The dataset contains relatively **few very low-priced laptops**.
- Since Random Forest cannot extrapolate beyond the patterns it has seen during training, predictions for low-end specifications are often **biased toward mid-range prices**.

---

## Model Performance

| Model | R² Score | MAE |
|------|------|------|
| Linear Regression (log target) | ~0.74 | 228 |
| Random Forest Regressor | ~0.81 | 190 |

---

## Installation
1. Clone the repository
```bash
git clone https://github.com/sumitadhikari7/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```
2. Install required packages
```bash
pip install -r requirements.txt
```
3. Run the Application
Start the Streamlit application using the following command.
```bash
streamlit run app.py
```
4. Open in Browser
After running the command, the application will automatically open in your browser at:
```bash
http://localhost:8501
```

## Conclusion
Due to these observations:
- **Linear Regression was excluded from the final deployment.**
- **Random Forest was selected as the final model** because it provides more stable and realistic predictions for most laptop configurations.

---