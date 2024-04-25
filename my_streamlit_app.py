import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv", sep=',')


continent_selection = st.sidebar.multiselect('Select Continent(s)', df['continent'].unique())
filtered_df = df[df['continent'].isin(continent_selection)] if continent_selection else df
st.write(filtered_df)

st.write('(Attention, ça prends un peu de temps pour afficher les plots !)')



st.write("Analyses de distribution et correlations par region:")
fig = sns.pairplot(filtered_df, hue='continent')
st.pyplot(fig.fig)

