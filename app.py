#chawanee sungthong
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/onlineretail_feb2010.csv')

st.title("Dashboard")
st.header("Sample Dataset")
st.dataframe(df.head(5))



df_pv = df.pivot_table(
    values = 'Quantity',
    index = 'Country',
    aggfunc= 'sum',
    ).sort_values('Quantity',ascending=False)


# slider
top = st.slider("Select Top", 5, 20)
st.write('Top' , top)
filtered_df = df_pv.head(top)

st.header('Pivot Table')
st.dataframe(filtered_df)

st.header("Sales Volume by Country (Top5)")
fig = px.bar(filtered_df)
st.plotly_chart(fig)


