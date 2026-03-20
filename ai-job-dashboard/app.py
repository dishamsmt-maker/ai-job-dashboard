import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My AI Job Dashboard")
st.write("ยินดีต้อนรับสู่ Dashboard ของผมครับ")

# ข้อมูลตัวอย่าง
data = pd.DataFrame({
    "Language": ["Python", "SQL", "Java", "C++", "JavaScript"],
    "Popularity": [90, 70, 50, 40, 65]
})

# แสดงตาราง
st.write("### ข้อมูลความนิยมภาษาโปรแกรม", data)

# กราฟแท่ง (Bar Chart)
fig1 = px.bar(data, x="Language", y="Popularity", title="Language Popularity")
st.plotly_chart(fig1)