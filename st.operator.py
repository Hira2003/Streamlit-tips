import streamlit as st

try:
  i = int(st.text_input('num1=',""))
except:
    st.write("fill in numbers first")
try:
  j = int(st.text_input('num2=',""))
except:
    st.write("fill in numbers first")
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


