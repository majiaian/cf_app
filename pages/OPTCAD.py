import streamlit as st

def calculate_opt_cad_score(age, history_myocardial_infarction, history_stroke, heart_rate, hypertension_history, ecg_st_segment_change, egfr, anemia, troponin_increase, lvef):
    score = 0
    
    # 年龄得分
    if age < 30:
        score += 0
    elif 30 <= age <= 39:
        score += 6
    elif 40 <= age <= 49:
        score += 19
    elif 50 <= age <= 59:
        score += 32
    elif 60 <= age <= 69:
        score += 45
    elif 70 <= age <= 79:
        score += 58
    else:  # age >= 80
        score += 71
    
    # 心肌梗死史得分
    if history_myocardial_infarction:
        score += 16
    
    # 卒中史得分
    if history_stroke:
        score += 16
    
    # 心率得分
    if heart_rate < 50:
        score += 24
    elif 50 <= heart_rate <= 79:
        score += 0
    elif 80 <= heart_rate <= 99:
        score += 12
    elif 100 <= heart_rate <= 119:
        score += 22
    else:  # heart_rate >= 120
        score += 36
    
    # 高血压病史得分
    if hypertension_history == 2:
        score += 11
    elif hypertension_history == 3:
        score += 20
    
    # 心电图ST段改变得分
    if ecg_st_segment_change:
        score += 13
    
    # eGFR得分
    if egfr < 60:
        score += 21
    
    # 贫血得分
    if anemia:
        score += 19
    
    # 心肌肌钙蛋白升高得分
    if troponin_increase:
        score += 23
    
    # LVEF得分
    if lvef < 50:
        score += 22
    
    return score

def risk_classification(score):
    if score <= 90:
        return "低危"
    elif 91 <= score <= 150:
        return "中危"
    else:  # score >= 151
        return "高危"

st.title("OPT-CAD评分计算器")

# 用户输入
age = st.slider("年龄（岁）", 0, 100, 65)
history_myocardial_infarction = st.checkbox("是否有心肌梗死史", value=False)
history_stroke = st.checkbox("是否有卒中史", value=False)
heart_rate = st.slider("心率（次/min）", 20, 200, 70)
hypertension_history = st.selectbox("高血压病史", ["否", "1级", "2级", "3级"], index=0)
hypertension_history = 0 if hypertension_history == "否" else int(hypertension_history[-1])
ecg_st_segment_change = st.checkbox("心电图ST段改变", value=False)
egfr = st.slider("eGFR（ml·min⁻¹·1.73 m⁻²）", 0, 100, 75)
anemia = st.checkbox("是否有贫血", value=False)
troponin_increase = st.checkbox("心肌肌钙蛋白是否升高", value=False)
lvef = st.slider("LVEF（%）", 20, 80, 55)

# 计算得分
score = calculate_opt_cad_score(age, history_myocardial_infarction, history_stroke, heart_rate, hypertension_history, ecg_st_segment_change, egfr, anemia, troponin_increase, lvef)

# 风险分级
risk = risk_classification(score)

# 显示结果
st.write("OPT-CAD评分：", score)
st.write("缺血风险分级：", risk)