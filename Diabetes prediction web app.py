# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:44:31 2023

@author: HRIDIMA K AJAY
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/HRIDIMA K AJAY/Desktop/Works/projects/diabetes prediction system/trained_model.sav','rb'))

#Creating a function for prediction

def diabetes_prediction(input_data):
    
    #changing the input data to numpy array
    arr=np.asarray(input_data)
    
    # reshaping input array as we are predicting for one instance
    reshaped=arr.reshape(1,-1)
    pred=loaded_model.predict(reshaped)
    print(pred)

    if(pred[0]==0):
      return "person is not diabetic"
    else:
      return "person is diabetic"
  
def main():
    
    # Title for web page
    st.title(" Diabetes Prediction App ")
    
    #Getting the input data from users for each variables
 
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Blood glucose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    # Prediction
    diagnosis=''
    
    #Creating a button for prediction
    if st.button('Diabetes Test Result'):
        
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
  
    st.success(diagnosis)
    
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    