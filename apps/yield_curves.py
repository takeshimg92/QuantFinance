import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

st.title('LTN yield curves')

data = pd.read_parquet('../_data/bonds.pqt')
dates = data['Dia'].unique()
total = len(dates)

i_date = st.slider("Date", min_value=0, max_value=total, value=0, step=1)
date = dates[i_date]


t= pd.to_datetime(str(date)) 
timestring = t.strftime('%d/%m/%Y')

st.write(timestring)

aux = data[data['Dia'] == date]

fig, ax = plt.subplots(figsize=(10,5))
aux.set_index('tenor')['YTM'].plot(ax=ax)
ax.set_xlim(0,6)
ax.set_ylim(-0.01,0.3)
st.pyplot(fig)