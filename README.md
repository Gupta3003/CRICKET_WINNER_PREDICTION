# 🏏 IPL 2025 Target Chase Predictor

This project uses **Machine Learning** to predict whether a team will successfully chase the target score in an IPL 2025 match based on the first innings score. It includes a data-driven ML model, a training notebook, and a Streamlit web app for predictions.

## 📁 Project Structure

```
ipl_2025_chase_predictor/
├── ML Notebook/
│   ├── ipl_target_chase_predictor.ipynb
│   └── model.pkl
├── app.py
├── data/
│   ├── deliveries.csv
│   └── matches.csv
├── requirements.txt
└── README.md
```

## Demo Vedio
https://github.com/user-attachments/assets/3cbcdea0-4f69-4e7a-a424-e4813f1161e9


## Screenshorts
|UI Page                                                                                             |UI Page                                                                                             |Result Page                                                                                       |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|  
|![Screenshot (982)](https://github.com/user-attachments/assets/59737654-032c-4b36-a147-208cf8e829eb)|![Screenshot (983)](https://github.com/user-attachments/assets/3ae6c293-adc6-4861-9a74-5c514c7d12c7)|![Screenshot (984)](https://github.com/user-attachments/assets/9c2709df-735d-457d-869d-0e8471b45279)|

## 📊 Datasets

- `matches.csv`: Match-level summary (teams, venue, toss, winner, result).
- `deliveries.csv`: Ball-by-ball delivery data with batsman, bowler, runs, etc.

## 🧠 Objective

To predict whether the team batting second will **chase** the target successfully or **not**, based on:
- First innings score
- Venue
- Teams playing
- Toss winner and decision

## ⚙️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 🛠️ Installation & Setup

1. **Clone this repository** or download the ZIP:

```bash
git clone https://github.com/yourusername/ipl_2025_chase_predictor.git
cd ipl_2025_chase_predictor
```

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install required packages**:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:
```bash
pip install streamlit pandas scikit-learn numpy
```

## 🚀 How to Run the App

After installing the dependencies, run the Streamlit app with:

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit in your browser (usually http://localhost:8501).

## 🧪 Model Training

To explore or retrain the model:

1. Open the Jupyter notebook:
```bash
jupyter notebook ML\Notebook\ipl_target_chase_predictor.ipynb
```

2. Run all cells to prepare the dataset, train the model, and export the `.pkl` file.

## 📌 Notes

- This model is trained using IPL-style data from past seasons.
- Model accuracy and results depend heavily on feature engineering and clean data.
