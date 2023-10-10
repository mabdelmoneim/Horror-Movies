import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',
                  page_title = 'dashboard')

tab1, tab2, tab3 = st.tabs(['descriptive statistics', 'numerical charts', 'categorical chart'])

df = pd.read_csv(r"D:\epsilon course\datasets\horror.csv")
box = st.sidebar.checkbox('show data', False ,key =1)
num = df.describe()
cat = df.describe(include="O")



if box:
    st.header('sample data')
    st.dataframe(df.head(10))

with tab1:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('categorical descriptive statistics')
        st.dataframe(cat)
        
    with col3:
        st.subheader('numerical descriptive statistics')
        st.dataframe(num)
with tab2:
    month = st.sidebar.selectbox('select month',df['month'].unique())
    vote = st.sidebar.selectbox('select vote',df['vote_average'].unique())
    col1,col2,col3 = st.columns(3)
    with col1:
        new_df = df[df['month'] == month]
        fig =  px.bar(df, x='month',  title= f'Count of Movies by Release month'.title())
        st.plotly_chart(fig,use_container_width=True)
        fig = px.bar(new_df, x ='month', y = 'revenue', color = 'vote_average',title = f'revenue for {month} month'.title())
        st.plotly_chart(fig,use_container_width=True)
        new_df1 = df[df['vote_average'] == vote]
        fig = px.histogram(new_df1, x= 'vote_average',title = f'Distribution of vote average'.title())
        st.plotly_chart(fig,use_container_width=True)
        
with tab3:
    original_language = st.sidebar.selectbox('select movie name',df['original_language'].unique())
    genre_name = st.sidebar.selectbox('select genre name',df['genre_names'].unique())
    col1,col2,col3 = st.columns(3)
    with col1:
        df_new2 = df[df['original_language'] == original_language]
        fig = px.scatter(df_new2, x='popularity', y='vote_average', hover_data=['original_language'])
        st.plotly_chart(fig,use_container_width=True)
        df_new3 = df[df['genre_names'] == genre_name]
    with col3:
        fig = px.bar(df_new3, x='genre_names', y='popularity')
        st.plotly_chart(fig,use_container_width = True)
