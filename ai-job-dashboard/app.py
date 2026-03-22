import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="My AI Dashboard", layout="wide")

# ส่วนหัว
st.title("AI Dashhhhh")
st.balloons()
st.sidebar.header("การตั้งค่าเมนู")
user_name = st.sidebar.text_input("กรอกชื่อผู้ใช้งาน:", "Disham")
st.sidebar.write(f"สวัสดีคุณ {user_name}!")

# ข้อมูลตัวอย่าง (Mock Data)
data = pd.DataFrame({
    "Language": ["Python", "SQL", "Java", "C++", "JavaScript", "Go", "R"],
    "Popularity": [95, 80, 60, 45, 70, 40, 35],
    "Ease_of_Use": [10, 8, 5, 3, 7, 6, 4]
})

# 1. ตัว Interactive (Sidebar Filter)
# เมื่อเลือกใน Sidebar กราฟข้างล่างจะเปลี่ยนตาม (ตรงตามเงื่อนไข interactive ระหว่าง components)
selected_lang = st.sidebar.multiselect(
    
    "เลือกภาษาโปรแกรมที่ต้องการดูข้อมูล:",
    options=data["Language"].tolist(),
    default=data["Language"].tolist()
)

# กรองข้อมูลตามที่เลือก
score_range = st.sidebar.slider("กรองช่วงคะแนนความนิยม:", 0, 100, (0, 100))
filtered_df = filtered_df[(filtered_df['Popularity'] >= score_range[0]) & (filtered_df['Popularity'] <= score_range[1])]
filtered_df = data[data["Language"].isin(selected_lang)]

# แบ่ง Layout เป็น 2 คอลัมน์
col1, col2 = st.columns(2)

with col1:
    # 2. กราฟที่ 1: Bar Chart (ยอดนิยม)
    st.subheader(" ความนิยมของภาษา")
    fig1 = px.bar(filtered_df, x="Language", y="Popularity", color="Language", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig1, use_container_width=True)
    st.info(f"💡 กราฟแท่งแสดงความนิยมของภาษาที่เลือกสำหรับคุณ {user_name}")

with col2:
    # 3. กราฟที่ 2: Pie Chart (ส่วนแบ่ง)
    st.subheader("สัดส่วนข้อมูล")
    fig2 = px.pie(filtered_df, values="Popularity", names="Language")
    st.plotly_chart(fig2, use_container_width=True)

# 4. กราฟที่ 3: Scatter Plot (ความง่าย vs ความนิยม)
st.divider()
st.subheader(" ความง่ายในการเรียนรู้ vs ความนิยม")
fig3 = px.scatter(filtered_df, x="Ease_of_Use", y="Popularity", 
                 size="Popularity", color="Language", hover_name="Language")
st.plotly_chart(fig3, use_container_width=True)
st.metric(label="Total Languages", value=len(filtered_df))
st.balloons()
st.sidebar.info("Dashboard นี้อัปเดตอัตโนมัติ")

