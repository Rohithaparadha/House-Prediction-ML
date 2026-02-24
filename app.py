

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load accuracy
with open("accuracy.txt", "r") as f:
    accuracy = f.read()


@app.route('/')
def home():
    return render_template('index.html', accuracy=accuracy)


@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])

    import pandas as pd
    input_data = pd.DataFrame([[area]], columns=['Area'])

    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return render_template('result.html', prediction=output, accuracy=accuracy)


if __name__ == '__main__':
    app.run(debug=True)