# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model=pickle.load(open('C:/Users/HRIDIMA K AJAY/Desktop/Works/projects/diabetes prediction system/trained_model.sav','rb'))

input_data=(5,166,72,19,175,25.8,0.587,51)
arr=np.asarray(input_data)
reshaped=arr.reshape(1,-1)
pred=loaded_model.predict(reshaped)
print(pred)
if(pred[0]==0):
  print("person is not diabetic")
else:
  print("person is diabetic")