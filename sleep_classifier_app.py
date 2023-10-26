# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 06:08:49 2023

@author: Gregory Bazuaye
"""

import numpy as np
import pandas as pd
import flask as Flask
import pickle
import streamlit as st


pickle_in = open('sleep_classifier.pkl' , 'rb')
classifier = pickle.load(pickle_in)


def predict_note_authenticity( gender , age , occupation , sleep_quality , physical_activity ,stress_level , bmi , blood_pressure , systolic , diastolic) :
     prediction = classifier.predict([[gender , age , occupation , sleep_quality , physical_activity ,stress_level , bmi , blood_pressure , systolic , diastolic]])
     if (prediction == 0):
        return 'The person suffers from sleep disorder'
     else :
        return 'The person does not suffer from a sleep disorder'
    
    
def main():
    st.header('Sleep Disorder Predictor')
    html_temp = """
    <div style="background-color: tomato; padding: 10px;">
    <h2 style="text-align: center; color: white;">Bank Authenticator</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    gender = (st.text_input('Gender', ''))
    age = (st.text_input('Age', ''))
    occupation = (st.text_input('Occupation', ''))
    sleep_quality = (st.text_input('Sleep Quality', ''))
    physical_activity =(st.text_input('Physical Acticvity Level', ''))
    blood_pressure = (st.text_input('Blood pressure', ''))
    systolic = (st.text_input('Systolic', ''))
    diastolic = (st.text_input('Diastolic', ''))
    prediction = ''  # Initialize prediction variable
    
    if st.button ('Predict') :
      

        age = float(age)
        
        sleep_quality = float(sleep_quality)
        physical_activity = float(physical_activity)
        systolic = float(systolic)
        diastolic = float(diastolic)
      
        prediction= predict_note_authenticity(variance , skewness , curtosis , entropy)
    
        st.success(f'The prediction is {prediction}')
    else :
          return 'Please enter values for all input fields'
    
    if st.button('About'):
        st.text("Let's learn")
        st.text('Built with Streamlit')
    
    
def is_valid(value):
    try :
        float(value)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    main()
    
    
    