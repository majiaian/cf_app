import streamlit as st

def calculate_lrinec_score(crp, wbc, hemoglobin, sodium, creatinine, glucose):
    score = 0

    if crp == ">=150":
        score += 4
    elif crp == "<150":
        score += 0

    if wbc == "<15":
        score += 0
    elif wbc == "15-25":
        score += 1
    elif wbc == ">25":
        score += 2

    if hemoglobin == ">13.5":
        score += 0
    elif hemoglobin == "11.0-13.5":
        score += 1
    elif hemoglobin == "<11":
        score += 2

    if sodium == ">=135":
        score += 0
    elif sodium == "<135":
        score += 2

    if creatinine == "<=141":
        score += 0
    elif creatinine == ">141":
        score += 2

    if glucose == "<=10":
        score += 0
    elif glucose == ">10":
        score += 1

    return score

# Streamlit 应用程序
st.title("坏死性筋膜炎 LRINEC 评分")
st.write("请选择以下实验室指标的范围以计算 LRINEC 评分：")

# 选择框
crp = st.radio("CRP (mg/L)", ["<150", ">=150"])
wbc = st.radio("白细胞计数 (个/mm³)", ["<15", "15-25", ">25"])
hemoglobin = st.radio("血红蛋白 (g/dL)", [">13.5", "11.0-13.5", "<11"])
sodium = st.radio("血钠 (mmol/L)", [">=135", "<135"])
creatinine = st.radio("血肌酐 (μmol/L)", ["<=141", ">141"])
glucose = st.radio("血糖 (mmol/L)", ["<=10", ">10"])

# 动态评分说明
st.write("评分说明：")
st.write("- CRP >= 150: +4 分")
st.write("- 白细胞计数 < 15: +0 分，15 <= 白细胞计数 <= 25: +1 分，白细胞计数 > 25: +2 分")
st.write("- 血红蛋白 > 13.5: +0 分，11.0 <= 血红蛋白 <= 13.5: +1 分，血红蛋白 < 11: +2 分")
st.write("- 血钠 >= 135: +0 分，血钠 < 135: +2 分")
st.write("- 血肌酐 <= 141: +0 分，血肌酐 > 141: +2 分")
st.write("- 血糖 <= 10: +0 分，血糖 > 10: +1 分")

# 计算按钮
if st.button("计算 LRINEC 评分"):
    score = calculate_lrinec_score(crp, wbc, hemoglobin, sodium, creatinine, glucose)
    st.write(f"LRINEC Score: {score}")

    # 判断条件
    if score >= 8:
        st.write("高度预示坏死性筋膜炎")
    elif score >= 6:
        st.write("疑似坏死性筋膜炎")
    else:
        st.write("评分较低，未达到疑似或高度预示标准")
