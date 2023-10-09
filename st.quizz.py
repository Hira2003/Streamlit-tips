import streamlit as st

i=1

st.title(f"Quest{i}")
st.write("what's the capital of Japan")
a = st.button("Hokaido")
if a:
  st.write("not right retry")
if st.button("Shikago"):
  st.write("not right retry")
if st.button("Seoul"):
  st.write("not right retry")
if st.button("Tokyo"):
  st.write("Cool! Right answer")
  i+=1
  if st.button("Next"):
      st.title(f"Quest{i}")
      st.write("what's the easiest programming language")
      a = st.button("Java")
      if a:
           st.write("not right retry")
      if st.button("SQL"):
          st.write("not right retry")
      if st.button("Javascript"):
          st.write("not right retry")
      if st.button("Python"):
          st.write("Cool! Right answer")
          i+=1


