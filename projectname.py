import streamlit as st
st.write("how do i get whole thing to streamlit, yeah")

st.text("yeahhh budddyy")
number = st.number_input("Enter a number:", min_value=0, max_value=100, value=10)
# Performing calculations
result = number * 2  # You can replace this with more complex logic if needed

# Displaying output
st.write("The result of multiplying your number by 2 is:", result)

# Displaying other messages or code results
st.write("This is a normal message displayed in Streamlit.")

