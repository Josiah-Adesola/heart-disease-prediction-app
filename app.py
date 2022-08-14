

import numpy as np
import pickle
import pandas as pd

import streamlit as st

#loading the saved model


loaded_model = pickle.load(open("trained_model.sav", 'rb'))

documentation_data = "https://archive.ics.uci.edu/ml/datasets/heart+disease"

some = """
id (Unique id for each patient)
age (Age of the patient in years)
origin (place of study)
sex (Male/Female)
cp chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic])
trestbps resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital))
chol (serum cholesterol in mg/dl)
fbs (if fasting blood sugar > 120 mg/dl)
restecg (resting electrocardiographic results)
-- Values: [normal, stt abnormality, lv hypertrophy]
thalach: maximum heart rate achieved
exang: exercise-induced angina (True/ False)
oldpeak: ST depression induced by exercise relative to rest
slope: the slope of the peak exercise ST segment
ca: number of major vessels (0-3) colored by fluoroscopy
thal: [normal; fixed defect; reversible defect]
num: the predicted attribute

"""
#creating the function for prediction

def heart_prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    if sex == 'Female':
        sex = 0
    elif sex == 'Male':
        sex = 1

    if cp == 'Typical angina':
        cp = 0
    elif cp == 'Atypical angina':
        cp = 1
    elif cp == 'Non-angina':
        cp = 2
    elif cp == 'Asymptomatic':
        cp = 3

    if fbs == "True":
        fbs = 1
    elif fbs == "False":
        fbs = 0

    if restecg == "Normal":
        restecg = 0
    elif restecg == "Stt abnormality":
        restecg = 1
    elif restecg == "Iv hypertrophy":
        restecg = 2
    
    if exang == "True":
        exang = 1
    elif exang == "False":
        exang = 0

    if thal== "Normal":
        thal = 0
    elif thal == "Fixed":
        thal = 1
    elif thal == "Defect":
        thal = 2
    elif thal == "Reversible Defect":
        thal = 3
    # data = input_data.reshape(1, -1)

    prediction = loaded_model.predict(pd.DataFrame([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]))

    if (prediction[0] == 0):
        print("The person doesn't have heart disease")
    else:
        print("The person has a heart disease")
    return prediction

    # if (prediction[0] == 0):
    #     print("The person doesn't have heart disease")
    # else:
    #     print("The person has a heart disease")



def main():

    st.title('Heart Disease Prediction Web App')
    st.markdown("This project was developed by Josiah Adesola")
    st.header("Heart Disease")
    st.markdown("Heart disease can be caused by various effects, and it's symptoms ranges from person to persons, across sex, age and race. This predictive app is just for learning purposes and give some insights on how some symptoms can influence heart dieseases")

    st.image("heart_disease.jpg")

    #get data from user
    age = st.number_input("Age", min_value=18, max_value=85, value=18)
    sex = st.selectbox("Gender", ["Female", "Male"])
    cp = st.selectbox("Chest Pain type", ['Typical angina', 'Atypical angina', 'Non-angina', 'Asymptomatic'])
    trestbps = st.number_input("Resting Blood Pressure (mm/Hg)", min_value=90, max_value=300, value=90)
    chol = st.number_input("Serum Cholesterol in mg/dl", min_value=100, max_value=650, value=150)
    fbs = st.selectbox("Fastig Blood Sugar", ["True", "False"])
    st.caption("Is it greater than 120mg/dl")
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal","Stt abnormality","Iv hypertrophy"])
    thalach = st.number_input("Maximum heart rate achieved", min_value=50, max_value=250, value=60)
    exang = st.selectbox("Exercise Induced Angina?", ["True", "False"])
    oldpeak = st.number_input("ST Depression induced by exercise relative to rest",  min_value=0.0, max_value=6.5, value=1.0)
    slope = st.number_input("Slope of the peak", min_value=1, max_value=3, value=1)
    ca = st.number_input("Number of major vessels colored by flourosopy",min_value=0, max_value=3, value=1)
    thal = st.selectbox("Stage of Thalassemia Blood disorder", ["Normal", "Fixed", "Defect", "Reversible Defect"])

    #code for prediction
    diagnosis = ''

    #creating the button for prediction

    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

        if (diagnosis[0] == 0):
            st.success("Congratulations!!!,there's no heart disease")
        elif (diagnosis[0] == 1):
            st.warning("Sorry! there is an heart disease")

if __name__ == '__main__':
    main()
