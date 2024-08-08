import streamlit as st
import pandas as pd

# Define the file path
file_path = '/Users/annie/Documents/DSC205/Celt_Reg_P_Stats.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the data in Streamlit
st.title("Celtics Regular Season Player Stats")
st.write("### Data from Excel File")
st.dataframe(df)

# Display the first 19 rows
st.write("### First 19 Rows")
st.dataframe(df.head(19))
