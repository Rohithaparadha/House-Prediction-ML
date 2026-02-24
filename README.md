🏠 House Price Prediction Web Application

A simple end-to-end Machine Learning web application that predicts house prices based on area (in square feet) using Linear Regression. The project covers data training, model evaluation, model serialization, and deployment using Flask.

📌 Project Overview

This application:

Trains a Linear Regression model using housing data

Evaluates performance using R² score

Saves the trained model using Pickle

Deploys the model through a Flask web interface

Accepts user input (house area) and returns predicted price

This project demonstrates the complete ML workflow from training to deployment.

🛠 Tech Stack

Python

Flask

Pandas

Scikit-learn

HTML / CSS

Pickle (Model Serialization)

📂 Project Structure
├── app.py              # Flask application
├── train_model.py      # Model training script
├── house_data.csv      # Dataset
├── model.pkl           # Saved ML model
├── accuracy.txt        # Stored R² score
├── templates/
│   ├── index.html
│   └── result.html
⚙️ How It Works
1️⃣ Model Training

Loads dataset (house_data.csv)

Splits into training and testing sets

Trains a Linear Regression model

Evaluates using R² Score

Saves:

model.pkl

accuracy.txt

Run:

python train_model.py
2️⃣ Run the Web Application
python app.py

Then open:

http://127.0.0.1:5000/
📊 Model Performance

Evaluation Metric: R² Score

Stored in: accuracy.txt

Displayed on the web interface

Note: If your R² score shows 1.0, it likely means your dataset is too small or perfectly linear. In real-world datasets, expect lower values.

🚀 Features

Clean web UI

Real-time prediction

Model accuracy display

Simple and lightweight deployment

Beginner-friendly ML deployment example

🔍 What This Project Demonstrates

Data preprocessing using Pandas

Train-test split

Linear Regression modeling

Model evaluation

Model persistence using Pickle

Flask routing and form handling

Integrating ML models into web apps

📈 Future Improvements

Add multiple input features (bedrooms, location, bathrooms)

Add proper error handling

Add model validation metrics (MAE, RMSE)

Deploy on cloud (Render / AWS / Railway)

Improve UI/UX

Add logging instead of debug mode

⚠️ Limitations

Uses only one feature (Area)

Not production-ready

No input validation

No security hardening

Assumes linear relationship
