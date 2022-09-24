import streamlit as st
import pandas as pd
st.info("This is info")

st.success("This is Success")

name = st.text_input("Enter your Name")

age = st.number_input("Enter your age")

height = st.slider("Enter your height" , min_value=0 , max_value=200 , value=100 , step=10)


dic = { "name":name , "age":age , "height":height}
df= pd.DataFrame(dic,index=[0])

st.write(df)