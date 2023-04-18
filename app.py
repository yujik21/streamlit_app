import streamlit as st


st. title('title of your application')
st.markdown('for example here is a **bold text**')


st.sidebar.title('title of the sidebar')

agree = st.checkbox('I agree')
disagree = st.checkbox("I disagree")

if agree:
    st.write('Great!')
if disagree:
    st.write('Bruhhhhhhh')

side_check = st.sidebar.checkbox('I agree yes yes')
if side_check:
    st.write('Sidebar checkbox has been clicked')
