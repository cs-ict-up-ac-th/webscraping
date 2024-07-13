import streamlit as st

st.title("🏆My first Data Science app!")

# placeholder = st.empty()
# status = 1

# if status == 1:
#     placeholder.success("Success!")
# else:
#     placeholder.error("Error!")


placeholder = st.empty()

status = st.radio(
    "Select an option:",
    ["Success", "Error"],
)

if status == "Success":
    placeholder.success("Success!")
else:
    placeholder.error("Oh Nooooo!")

# st.info("Show Information!")
# st.success("Show Success")
# st.error("Show Error")
# st.warning("Show Warning")

import pandas as pd
import numpy as np

st.header("Area chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

import altair as alt

source = df

c = alt.Chart(source).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='body_mass_g',
    color='species',
).interactive()

st.altair_chart(c, use_container_width=True)