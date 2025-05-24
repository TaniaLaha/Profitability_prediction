from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

df = pd.read_csv("profitable.csv", index_col=0)
feature_names = df.drop(columns=["class"]).columns.tolist()

@app.route('/')
def home():
    return render_template("index.html", feature_names=feature_names)

@app.route('/predict', methods=["POST"])
def predict():
    try:
        input_data = [request.form.get(f) for f in feature_names]
        df_input = pd.DataFrame([input_data], columns=feature_names)
        df_input = df_input.apply(pd.to_numeric, errors='ignore')
        prediction = model.predict(df_input)[0]
        result = "Profitable ✅" if prediction == 1 else "Not Profitable ❌"
    except Exception as e:
        result = f"Error: {e}"
    return render_template("index.html", prediction_text=result, feature_names=feature_names)

if __name__ == '__main__':
    app.run(debug=True)
