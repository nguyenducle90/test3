pip install streamlit
pip install networkx

import sklearn
import os
import pickle
import streamlit as st

Filepath = os.path.join(os.getcwd(),'gold.model.pkl')
def forecast(spx: float, uso: float, slv: float, eur_usd: float) -> float:
    model = pickle.load(open(Filepath, 'rb'))
    results = model.predict([[spx, uso, slv, eur_usd]])
    return results[0]

st.header('kết quả dự đoán giá vàng')
spx = st.slider('SPX', min_value=676.0, max_value=2873.0, step=0.1)
uso = st.slider('USO', min_value=8.0, max_value=118.0, step=0.1)
slv = st.slider('SLV', min_value=9.0, max_value=48.0, step=0.1)
eur_usd = st.slider('EUR/USD', min_value=1.0, max_value=2.0, step=0.1)
results = forecast(spx, uso, slv, eur_usd)
st.write('Predicted:%s' % results)
