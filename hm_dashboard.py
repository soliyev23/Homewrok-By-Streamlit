import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("fifa_players.csv")

st.title("Assalomu Alaykum weclome to my first dashboard application😎")
st.write("### Here you can get any statistic information about football players.")


if st.button("Show DataFrame"):
    st.dataframe(df)
    if st.button("Clean "):
        st.write("All is cleaned")

tab_1, tab_2 = st.tabs(["CountPlot", "HistPlot"])

with tab_1:
    st.header("Countplot")
    
    fig, ax = plt.subplots()
    temp = sns.countplot(x=df["national_team"].iloc[:20],ax=ax,hue=df["national_team"].iloc[:20])
    ax.set_xticklabels(df["national_team"], rotation=40)
    ax.set_title("National Team")
    st.pyplot(fig)

with tab_2:
    st.header("Histplot")
    fig, ax = plt.subplots()
    temp_1 = sns.histplot(x=df["preferred_foot"].head(20))
    st.pyplot(fig)


    
        








