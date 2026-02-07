import streamlit as st

st.set_page_config(page_title="โปรแกรมคำนวณเกรด", page_icon="📝")

st.title("📝 โปรแกรมคำนวณเกรดภาษาจีน")
st.write("สวัสดีครับนักเรียน! กรอกคะแนนเพื่อเช็คเกรดได้เลย")

# รับข้อมูล
col1, col2 = st.columns(2)
with col1:
    score_collect = st.number_input("คะแนนเก็บ (เต็ม 80)", min_value=0, max_value=80, step=1)
with col2:
    score_final = st.number_input("คะแนนสอบ (เต็ม 20)", min_value=0, max_value=20, step=1)

# ปุ่มคำนวณ
if st.button("กดเพื่อดูเกรด", type="primary"):
    total_score = score_collect + score_final
    
    # คำนวณเกรด
    if total_score >= 80:
        grade = "4"
        color = "green"
        msg = "ยอดเยี่ยมมาก! 🎉"
    elif total_score >= 75:
        grade = "3.5"
        color = "blue"
        msg = "เก่งมากครับ! 👍"
    elif total_score >= 70:
        grade = "3"
        color = "blue"
        msg = "ทำได้ดีครับ!"
    elif total_score >= 60:
        grade = "2"
        color = "orange"
        msg = "ผ่านครับ พยายามต่อไป!"
    elif total_score >= 50:
        grade = "1"
        color = "orange"
        msg = "ผ่านเกณฑ์พอดีครับ"
    else:
        grade = "0"
        color = "red"
        msg = "พยายามใหม่เทอมหน้านะครับ สู้ๆ! ✌️"

    # แสดงผล
    st.divider()
    st.header(f"คะแนนรวม: {total_score} คะแนน")
    st.subheader(f"เกรดที่ได้: :{color}[{grade}]")
    st.caption(msg)
