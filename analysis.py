import pandas as pd 
import streamlit as st
import seaborn as sns
import time

df = pd.read_csv("fifa_players.csv")
# st.write(df)

c = df[df["national_team"] == "France"]
# st.write(c)
genre = st.radio(
    label = "What's your favorite movie genre",
    options = df["national_team_position"].unique(),
    index=None,
)

st.write("You selected:", genre)

st.dataframe(df)



st.line_chart(df["height_cm"].iloc[:100])


with st.sidebar:
    
    with st.echo():
        st.write("The Category of plots:")
        st.button("Lineplot",type="primary")

    with st.spinner("Loading..."):
        pass    
        time.sleep(5)
    st.success("Done!")




tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)