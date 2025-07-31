# DiabeCheckr – A Simple Diabetes Predictor 

**DiabeCheckr** is a beginner-friendly web application built using **Flask** that predicts whether a person is diabetic or not based on medical input. The prediction is powered by a **Random Forest Classifier** trained on the PIMA Indian Diabetes dataset.

---

## Web App Preview

![App Screenshot](preview.png)

---

### About the Model

- **Model**: Random Forest Classifier  
- **Trained on**: PIMA Indians Diabetes dataset  
- **Accuracy**: ~82%  
- **Features used**: Glucose, Insulin, BMI, Age  
- **Serialization**: `pickle` → `model.pkl`

---

#### How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/harrishsrinivasan/DiabeCheckr---A-Diabetes-Prediction-App-using-Machine-Learning.git
cd DiabeCheckr


###### Project Structure
```txt
├── DiabeCheckr/            # Flask web app (UI, routes, ML model)
│   ├── static/
|       |── style.css
│   ├── templates/
|       |── index.html
│   ├── app.py
│   ├── model.pkl
│ 
├── diabetes project.ipynb  # Model building & training
├── diabetes.csv            # Dataset used
├── preview.png             # Web app preview screenshot
└── README.md               # You're reading it!

---

