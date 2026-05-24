from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__)

# Load and preprocess data
def load_and_preprocess_data():
    # Load city_day.csv
    data = pd.read_csv('city_day.csv')
    
    # Handle missing values: fill with mean for numeric columns, drop rows with no AQI
    numeric_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
    data = data.dropna(subset=['AQI'])  # Keep only rows with AQI
    
    return data

# Load and prepare data
data = load_and_preprocess_data()

# Debug: Print column names and first few rows
print("Columns in CSV:", data.columns.tolist())
print("Data preview:\n", data.head())

# Train a Random Forest model
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]  # Select key pollutants
y = data['AQI']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# AQI to condition mapping with detailed categories
def aqi_to_condition(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    city = request.json.get('city')
    city_data = data[data['City'].str.lower() == city.lower()]
    
    if city_data.empty:
        return jsonify({'error': 'City not found'}), 404
    
    # Use the latest available data for the city
    latest_data = city_data.tail(1)
    features = latest_data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']].values
    predicted_aqi = model.predict(features)[0]
    condition = aqi_to_condition(predicted_aqi)
    
    # Include pollutant data in the response
    response = {
        'city': city,
        'aqi': round(predicted_aqi, 1),
        'pm25': round(latest_data['PM2.5'].values[0], 1) if not pd.isna(latest_data['PM2.5'].values[0]) else None,
        'pm10': round(latest_data['PM10'].values[0], 1) if not pd.isna(latest_data['PM10'].values[0]) else None,
        'no2': round(latest_data['NO2'].values[0], 1) if not pd.isna(latest_data['NO2'].values[0]) else None,
        'so2': round(latest_data['SO2'].values[0], 1) if not pd.isna(latest_data['SO2'].values[0]) else None,
        'co': round(latest_data['CO'].values[0], 1) if not pd.isna(latest_data['CO'].values[0]) else None,
        'o3': round(latest_data['O3'].values[0], 1) if not pd.isna(latest_data['O3'].values[0]) else None,
        'condition': condition
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)