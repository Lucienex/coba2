import streamlit as st
import pandas as pd
import numpy as np

st.title('Aplikasi Sederhana Streamlit')

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.dataframe(df)

st.write('Plot sederhana')
st.line_chart(df)