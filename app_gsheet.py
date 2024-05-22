# streamlit_app.py
import streamlit as st
from streamlit_gsheets import GSheetsConnection
# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet = "Sheet1",
    usecols=[0, 1],
    nrows=3,
)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
