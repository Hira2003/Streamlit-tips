import streamlit as st

try:
  i = int(st.text_input('num1=',""))
except:
    st.write("fill in numbers first")
try:
  j = int(st.text_input('num2=',""))
except:
    st.write("fill in numbers first")
c1, c2, c3, c4 = st.columns(2)
with c1:
  if(st.button('addition')):
    st.write(j,'+',i,'=',j+i)
    st.write(i,'+',j,'=',i+j)
with c2:
  if(st.button('substraction')):
    st.write(j,'-',i,'=',j-i)
    st.write(i,'-',j,'=',i-j)
with c3:
 if(st.button('multiplication')):
    st.write(j,'*',i,'=',j*i)
    st.write(i,'*',j,'=',i*j)
with c4:
 if(st.button('division')):
    st.write(j,'/',i,'=',j/i)
    st.write(i,'/',j,'=',i/j)


