import streamlit as st

i = int(st.text_input('num1=',""))
j = int(st.text_input('num2=',""))

if(st.button('addition')):
    st.write(j,'+',i,'=',j+i)
    st.write(i,'+',j,'=',i+j)
if(st.button('substraction')):
    st.write(j,'-',i,'=',j-i)
    st.write(i,'-',j,'=',i-j)
if(st.button('multiplication')):
    st.write(j,'*',i,'=',j*i)
    st.write(i,'*',j,'=',i*j)
if(st.button('division')):
    st.write(j,'/',i,'=',j/i)
    st.write(i,'/',j,'=',i/j)


