import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'apple_quality.csv'  # Update the path if necessary
data = pd.read_csv(file_path)

# Streamlit app
st.title('Apple Quality Visualization App')

# User inputs for selecting qualities
quality1 = st.selectbox('Select the first quality to compare:', data.columns[:-1], index=3)  # Default to 'Sweetness'
quality2 = st.selectbox('Select the second quality to compare:', data.columns[:-1], index=4)  # Default to 'Crunchiness'

# Plotting
st.write(f"Scatter Plot comparing {quality1} and {quality2}")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=quality1, y=quality2, hue='Quality', ax=ax)
plt.xlabel(quality1)
plt.ylabel(quality2)
st.pyplot(fig)

# Display data (optional)
if st.checkbox('Show raw data'):
    st.write(data)
