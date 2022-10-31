import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.write("Python Visualization ด้วย Streamlit")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data) #สร้างและแสดงกราฟเส้น
add_sidebar = st.sidebar.selectbox('Choose', ('Usage','Payment'))


st.header('Day5 สอนใช้ st.write') #เขียนหัวข้อ

# Example 1
st.write('Hello,ทำตัวหนา *World!* :sunglasses:') 

# Example 2
st.write(1234) #เขียนตัวเลข

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df) #เขียน data frame

# Example 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c) #วาดกราฟ

# st.slider


st.header('DAY 8 st.slider')

# Example 1

st.subheader('Slider')
st.write('Int')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')
st.write('Float')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')
st.write('time')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')
st.write('Datetime')
start_time = st.slider(
     "When do you start?",
     value=datetime(2022, 10, 1, 0, 0),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.header('Day 9 Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.header('Day 10 st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.header('Day 11 st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

st.header('Day 12 st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

# Day 14
st.header('Day 14 Component')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
pr = df.profile_report()
st_profile_report(pr)