import streamlit as st

st.title("title")
st.text("yo")

name = st.text_input("name","joe mama",key="input1")
nim = st.text_input("NIM","1234567890",key="input2")
address = st.text_input("Address","1st st.",key="input3")

selection = st.selectbox("Subject",['RPL','Alpro','ML'])

age = st.slider("Age",1,99,10)

hobby = st.text_area("Hobby","Football,Gaming")
hobby = [x.strip() for x in hobby.split(',')]

gender = st.radio("Gender",['male','female'])
if (gender=="male"):
    st.write("HI! Mr "+name)
else:
    st.write("HI! Ms "+name)

if (len(nim)==10):
    st.text("Name: "+name)
    st.text("NIM: "+nim)
    st.text("Address: "+address)
    st.write(selection)
    st.write(age)
    st.write(gender)
    st.write(hobby)
else:
    st.text("Please input the right data")

st.image('https://www.blibli.com/friends-backend/wp-content/uploads/2022/11/biodata-takashi-murakami.jpg',caption="yo")

st.markdown('[link to your favorite site](www.google.com)')

import pandas as pd

data = {'Occupation' : ['Programmer','Doctor','Lawyer']
        ,'Tier' : ['D','SS','A']}

df = pd.DataFrame(data)
st.dataframe(df)

st.title("Open Folder")
file = st.file_uploader("choose jpg",type=['jpg'])

if file is not None:
    st.write(file.type)
    if file.type == "image/jpg":
        st.image(file)
    else:
        data = pd.read_csv(file)

        st.dataframe(data)

st.title("Calculator")
num1 = st.number_input("input number 1: ",value=0)
num2 = st.number_input("input number 2: ",value=0)

operation = st.radio("Choose",['addition','subtraction','multiplication','division'])

if st.button("calculate"):
    if operation == 'addition:':
        result = num1 + num2
    elif operation == "subtraction":
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        result = num1 / num2

    st.success(f'result {operation} : {result}')

st.sidebar.header("feature on the left")

if st.sidebar.checkbox("Biodata"):
    st.sidebar.write(f"Name : {name}")