# streamlit_app.py
import streamlit as st
from streamlit_gsheets import GSheetsConnection
# Create a connection object.
url = "https://docs.google.com/spreadsheets/d/1L19AF2t_svkYHtRhAgxg0vLliIklD4wKlK3AwcgiN3o/edit#gid=0"
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    spreadsheet = url,
    worksheet = "Sheet1",
    usecols=[0, 1],
    nrows=3,
)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
