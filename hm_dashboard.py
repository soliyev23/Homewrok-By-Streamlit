import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("fifa_players.csv")

with st.sidebar:
    st.title("Here you can chohse the different types of plot.")

    with st.sidebar:
        add_radio = st.radio("Chose a type of plots", ("HOME","LINEPLOT", "BAR","BOXPLOT"))

if add_radio == "HOME":
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

        bin = st.select_slider(
        "Select Bin Number:",
        options=list(range(1, 30)))

        st.header("Histplot")
        fig, ax = plt.subplots()

        temp_2 = df.groupby(by="nationality")["height_cm"].mean().to_frame()

        temp_1 = sns.histplot(x=temp_2["height_cm"].head(100),ax=ax,color="y",kde=True,bins=bin)
        ax.set_title("The Height on (cm)")

        st.pyplot(fig)

if add_radio == "LINEPLOT":
    temp_df = sns.load_dataset("fmri")
    st.header("Line Plot")

    fig, ax = plt.subplots()
    # st.dataframe(temp_df)
    sns.lineplot(data=temp_df, x="timepoint", y="signal",color="y",size="region",style="region",markers=True)
    st.pyplot(fig)

if add_radio == "BAR":
    st.header("BAR PLOT")

    f_player_10 = df.iloc[:10]
    st.dataframe(f_player_10)

    fig, ax = plt.subplots()
    sns.barplot(data=f_player_10, x="name", y="age",hue="name",ax=ax,)
    ax.set_xticklabels(f_player_10["name"] ,rotation=20)
    ax.set_title("FootBall Player")
    st.pyplot(fig)

    st.write("## The Diogramm of Football Player By Age")


if add_radio == "BOXPLOT":
    st.header("BOXPLOT")
    # st.dataframe(df)

    fig,ax = plt.subplots(1,2, figsize=(12,5))
    sns.boxplot(data=df, y="weight_kgs",ax=ax[0],color="red")
    ax[0].set_title("Weights on (kg)")
    sns.boxplot(data=df, y="height_cm",ax=ax[1],color="green")
    ax[1].set_title("Height on (cm)")
    st.pyplot(fig)
    st.write("Here you can see the DIOGRAMM of players by (Weight) and (Height)")

    st.dataframe(df)






        










