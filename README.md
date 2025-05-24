
# **Algerian Forest Fire Prediction using Ridge Regression**

This project applies **Ridge Regression** to predict forest fire occurrence in **Bejaia** and **Sidi Bel-abbes, Algeria** using meteorological data. By mitigating multicollinearity, Ridge Regression enhances model stability and generalization.

## 📂 **Dataset Overview**
- **Source:** https://www.kaggle.com/datasets/nitinchoudhary012/algerian-forest-fires-dataset
- **Instances:** 244 (138 fire cases, 106 no-fire cases).
- **Features:** 
  - Temperature (°C)
  - Relative Humidity (%)
  - Wind Speed (km/h)
  - Rainfall (mm)
  - Fire Weather Index (FWI)

## 🎯 **Objective**
- Predict **fire occurrence** based on environmental conditions.
- Improve model performance by **reducing overfitting** using **Ridge Regression**.
- Aid authorities in fire prevention and resource allocation.

## 🛠 **Approach**
1. **Data Preprocessing:** Handling missing values and scaling features.
2. **Exploratory Data Analysis (EDA):** Identifying feature correlations.
3. **Feature Engineering:** Selecting impactful attributes.
4. **Model Training:** Implementing **Ridge Regression** for prediction.
5. **Evaluation:** Comparing Ridge Regression with **Linear Regression**, **Lasso**, and **Random Forest**.

## 🏆 **Results & Insights**
- Ridge Regression effectively handles **multicollinearity** and provides **stable predictions**.
- **Fire Weather Index (FWI)** is a strong predictor of fire risk.
- Model optimizations improve early detection and emergency planning.

## 🚀 **How to Run the Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/HanniKanchap/Algerian-Forest-Fire-Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis and model training:
   ```bash
   python ridge_regression.py
   ```
