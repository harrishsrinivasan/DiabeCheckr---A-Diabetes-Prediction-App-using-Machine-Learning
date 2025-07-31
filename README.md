# DiabeCheckr – A Simple Diabetes Predictor 

**DiabeCheckr** is a beginner-friendly web application built using **Flask** that predicts whether a person is diabetic or not based on medical input. The prediction is powered by a **Random Forest Classifier** trained on the PIMA Indian Diabetes dataset.

---

## Web App Preview

![App Screenshot](./3dc36fe7-7ca3-45df-a5a4-5f54f10dc1ee.png)

---

## Project Structure

├── DiabeCheckr/ # Flask web app (UI, routes, ML model)
│ ├── static/
│ ├── templates/
│ ├── app.py
│ ├── model.pkl
│ └── style.css / others
├── diabetes project.ipynb # Model building & training
├── diabetes.csv # Dataset used
├── README.md # You're reading it!

---

## About the Model

- **Model**: Random Forest Classifier  
- **Trained on**: PIMA Indians Diabetes dataset  
- **Accuracy**: ~82%  
- **Features used**: Glucose, Insulin, BMI, Age  
- **Serialization**: `pickle` → `model.pkl`

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DiabeCheckr.git
cd DiabeCheckr
