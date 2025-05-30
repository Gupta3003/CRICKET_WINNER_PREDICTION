# CRICKET_WINNER_PREDICTION
# 🏏 IPL 2025 Target Chase Predictor

This project uses **Machine Learning** to predict whether the target score set in the first innings of an IPL 2025 match will be **chased** or **not** in the second innings. The prediction is made based on historical match and delivery data from the Indian Premier League (IPL).

## 🔍 Project Structure


├── ML Notebook/
│ ├── ipl_target_chase_predictor.ipynb # Jupyter notebook for training and evaluating the model
│ └── model.pkl # Trained ML model saved using joblib or pickle
├── app.py # Streamlit web application
├── data/
│ ├── deliveries.csv # Ball-by-ball level data
│ └── matches.csv # Match-level summary data
└── README.md # Project documentation


## 🧠 Problem Statement

Given the **first innings score** and match context, predict whether the team batting second will be able to **chase** the target successfully.

## 📊 Data

- **matches.csv**: Contains match-level details such as match ID, teams, venue, toss decision, result, etc.
- **deliveries.csv**: Contains detailed delivery-by-delivery data, including runs, wickets, batsman, bowler, etc.

## 🛠️ Features Used

- First innings total score
- Venue
- Batting and bowling teams
- Toss winner and toss decision
- Match year
- Powerplay statistics (optional)

## 🧪 Model

A classification model is trained using scikit-learn (e.g., Random Forest, Logistic Regression) to predict the outcome:
- `1`: Target chased
- `0`: Target not chased

## 🚀 Running the App

### Prerequisites

Make sure you have Python 3.7+ installed.

### Install Requirements

```bash
pip install -r requirements.txt

pip install pandas numpy scikit-learn streamlit

