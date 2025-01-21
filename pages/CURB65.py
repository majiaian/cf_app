import streamlit as st

def curb65_score(confusion, bun, respiration_rate, low_bp, age_lt_65):
    score = 0
    if confusion:
        score += 1
    if bun >= 7:
        score += 1
    if respiration_rate >= 30:
        score += 1
    if low_bp:
        score += 1
    if not age_lt_65:
        score += 1
    return score


st.title("CURB-65 评分工具")

st.write("请填写以下信息以计算CURB-65评分：")

confusion = st.checkbox("是否出现意识障碍？")
bun = st.number_input("血尿素氮 (mmol/L)", min_value=0.0, value=0.0, step=0.1)
respiration_rate = st.number_input("呼吸频率 (次/分钟)", min_value=0, value=0, step=1)
low_bp = st.checkbox("是否低血压？")
age_lt_65 = st.checkbox("年龄是否小于65岁？")

if st.button("计算评分"):
    score = curb65_score(confusion, bun, respiration_rate, low_bp, age_lt_65)
    st.write(f"CURB-65 评分为：{score}")

    if score == 0:
        st.write("低风险")
    elif score == 1:
        st.write("中等风险")
    elif score >= 2:
        st.write("高风险")
