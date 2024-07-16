import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.preprocessing  import StandardScaler
import pickle


cat = pd.DataFrame({'misc_net':[8], 'grocery_pos':[4], 'entertainment':[0], 'gas_transport':[2],
       'misc_pos':[9], 'grocery_net':[3], 'shopping_net':[11], 'shopping_pos':[12],
       'food_dining' : [1], 'personal_care':[10], 'health_fitness':[5], 'travel':[13],
       'kids_pets':[7], 'home':[6]})
cat.to_dict()


model = pickle.load(open('model.pkl','rb'))

scaler = StandardScaler()
cc_num = st.number_input('Enter the Credit Number ',step =1 )

category = st.selectbox('Select Category',['misc_net', 'grocery_pos', 'entertainment', 'gas_transport',
       'misc_pos', 'grocery_net', 'shopping_net', 'shopping_pos',
       'food_dining', 'personal_care', 'health_fitness', 'travel',
       'kids_pets', 'home'])
category_text = cat.get(category)
amt = st.number_input('Enter the amount ')


gender =st.selectbox('Gender',['Male','Female'])

if gender =='Male':
    gender = 1
else :
    gender = 0 

zipcode = st.number_input('Enter the ZipCode ',step= 1)
date = st.date_input('Select the transaction date')

year = date.year
month = date.month
day = date.day 






    

query = pd.DataFrame([[cc_num,category_text,amt,gender,zipcode,
                      year,month,day]],
                    columns=['cc_num','category','amt','gender',
                             'zip','year','month',
                             'day'])

query_scaled = scaler.fit_transform(query)

result = model.predict(query_scaled)
if st.button('Predict'):
    if result == 0:
        st.header('Not a fraoud ') 
    else :
        st.header('Fraoud')