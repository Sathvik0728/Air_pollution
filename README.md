# 🌍 Air Pollution Prediction System

An AI-powered Air Pollution Prediction and Analysis web application developed using Flask, Machine Learning, and Indian AQI datasets.

The system predicts Air Quality Index (AQI) values based on pollutant concentrations and provides pollution insights for different cities using a clean and interactive web interface.

---

# 🚀 Features

✅ Air Quality Index (AQI) Prediction  
✅ Machine Learning-Based Analysis  
✅ City-wise Pollution Insights  
✅ Pollutant Level Monitoring  
✅ AQI Category Classification  
✅ Interactive User Interface  
✅ Real-world Indian AQI Dataset  
✅ Flask REST API Backend  

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Random Forest Regressor

## Data Processing
- Pandas
- NumPy

---

# 📂 Project Structure

```bash
Air_pollution/
│
├── static/
│   ├── styles.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
│
├── city_day.csv
├── city_hour.csv
├── station_day.csv
├── station_hour.csv
├── stations.csv
│
├── requirements.txt
├── README.md
└── .gitattributes
```

---

# 📊 Dataset Information

The project uses Indian Air Quality datasets containing pollutant information such as:

- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- Benzene
- Toluene
- Xylene
- AQI

Datasets Included:
- City-wise Daily AQI Data
- City-wise Hourly AQI Data
- Station-wise Daily AQI Data
- Station-wise Hourly AQI Data

---

# 🧠 Machine Learning Model

The application uses:

## Random Forest Regressor

The model is trained using major pollutant features:

```python
['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
```

The trained model predicts AQI values for selected cities.

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sathvik0728/Air_pollution.git
```

---

## 2️⃣ Move Into Project Directory

```bash
cd Air_pollution
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Application

```bash
python app.py
```

---

# 🌐 Open In Browser

```bash
http://127.0.0.1:5000
```

---

# 📈 AQI Categories

| AQI Range | Category |
|-----------|-----------|
| 0 – 50 | Good |
| 51 – 100 | Satisfactory |
| 101 – 200 | Moderate |
| 201 – 300 | Poor |
| 301 – 400 | Very Poor |
| 401+ | Severe |

---

# 🔄 Application Workflow

1. User enters city name
2. Flask API receives request
3. Dataset is filtered for the city
4. Machine Learning model predicts AQI
5. Pollutant details are displayed
6. AQI category is generated

---

# 💡 Future Improvements

- Real-Time AQI API Integration
- Interactive Data Visualization
- Deep Learning Models
- AQI Forecasting System
- Live Weather Integration
- Mobile Responsive Design
- Cloud Deployment

---

# ☁️ Deployment Platforms

This project can be deployed on:

- Render
- Railway
- PythonAnywhere
- Heroku
- VPS

# 👨‍💻 Author

## Banda Sathvik

Computer Science Engineering Student  
AI & ML Enthusiast  
Python Developer  

### GitHub
https://github.com/Sathvik0728

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
📢 Share with others  

---

# 📄 License

This project is created for educational and learning purposes.

---