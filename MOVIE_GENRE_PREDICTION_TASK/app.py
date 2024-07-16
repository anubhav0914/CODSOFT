import streamlit as st
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
import string

ps = PorterStemmer()

def trasform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text) # now it is a list
    y = []
    for i in text :
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text :
        y.append(ps.stem(i))
    return " ".join(y)
labels = ['action','adult','adventure','animation','biography','comedy','crime','documentary','drama','family','fantasy','game-show','history',
         'horror','music','musical','mystery','news','reality-tv','romance','sci-fi','short','sport','talk-show','thriller','war','western',]


tfid = pickle.load(open('hs.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Movie genre prediction')

input_sms = st.text_area("Enter the summary ")
if st.button('Predict'):
    trasform_sms = trasform_text(input_sms)
    vector_input = tfid.transform([trasform_sms])
    result = model.predict(vector_input)[0]
    st.header(labels[result])