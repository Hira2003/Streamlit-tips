import streamlit as st


#shorter code
st.write("please enter info to log in")
M= st.text_input("Username or Email","")
P= st.text_input("Password","")
N = st.text_input("Username for new users","")
    
#in reality also we are not going to show passwords right?
if st.button("login"):
    st.write("valid user",M)

if st.button("sign up"):
    st.write(M,"is new user added successfully as",N)
    #let's see