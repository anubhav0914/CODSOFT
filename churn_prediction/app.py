import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.preprocessing  import StandardScaler
import pickle


scaler = StandardScaler()

selected_gender = st.selectbox('Select Gender', ['Male','Female'])
GENDER_MALE = False
if selected_gender == 'Male':
    GENDER_MALE = True
selcet_Country = st.selectbox("select City",['Spain','France','Germany'])

Geo_spain =False
Geo_Germany = False 

if selcet_Country == 'Spain':
    Geo_spain = True
    Geo_Germany =False
elif selcet_Country == 'Germany':
    Geo_Germany = True
    Geo_spain = False
else :
    
    Geo_spain =False
    Geo_Germany = False 


Credit_Score = st.number_input("Enter Credit SCore")
Age  = st.number_input("Enter age")
Tenure = st.selectbox('Select Tenure',[0,1,2,3,4,5,6,7,8,9,10])
Balance = st.number_input("Enter Balance")
Num_of_product = st.selectbox('Select numer of product',[1,2,3,4])
hashCard = st.selectbox('Do the  customer has CrCard',['yes','No'])
hasCrCard = 0

if hashCard =='yes':
    hasCrCard = 1
else :
    hasCrCard = 0

isActive = st.selectbox('is   customer Active Member',['yes','No'])
isActiveMemb = 0
if isActive =='yes':
    isActiveMemb = 1
else :
    isActiveMemb = 0
    
salary = st.number_input('Enter the Esimated salary')

query = pd.DataFrame([[Credit_Score,	Age,Tenure,Balance,Num_of_product,
                      hasCrCard,isActiveMemb,salary,Geo_Germany,Geo_spain,GENDER_MALE]],
                    columns=['CreditScore','Age','Tenure','Balance',
                             'NumOfProducts','HasCrCard','IsActiveMember',
                             'EstimatedSalary','Geography_Germany',
                             'Geography_Spain','Gender_Male'])

query_scaled = scaler.fit_transform(query)
model = pickle.load(open('model.pkl','rb'))

result = model.predict(query_scaled)
if st.button('Predict'):
    if result == 0:
        st.header('Exited ') 
    else :
        st.header('Not Exited')