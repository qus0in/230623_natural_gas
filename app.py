import streamlit as st

import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/qus0in/natural_gas/main/%ED%95%9C%EA%B5%AD%EA%B0%80%EC%8A%A4%EA%B3%B5%EC%82%AC_%EC%9B%94%EB%B3%84%20%EC%B2%9C%EC%97%B0%EA%B0%80%EC%8A%A4%20%EC%83%9D%EC%82%B0%EB%9F%89_20221031.csv",
    encoding='cp949'
)
# df

import seaborn as sns

df['연월'] = df.apply(lambda x: str(int(x.연도))[2:] + '-' + str(int(x.월)).zfill(2), axis=1)
# df

plot = sns.lineplot(df, x='연월', y='생산량')

st.pyplot(plot.figure)