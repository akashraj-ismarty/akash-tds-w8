import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome All"

def main():
  st.title("EVEN or ODD")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:blue;text-align:center;">Finding even or odd number using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  
  num1 = st.number_input("Please enter the number here:")
  if (num1%2==0):
    st.success('{} is an even number'.format(num1))
  else:
    st.success('{} is an odd number'.format(num1))
  
  if st.button("Made By"):
      st.text("K AKASH")
      st.text("21F1004520")

if __name__=='__main__':
  main()