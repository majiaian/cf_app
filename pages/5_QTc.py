import streamlit as st
import pandas as pd
import numpy as np

# 定义QTc计算函数
def calculate_qtc(qt_interval, rr_interval, heart_rate):
    if heart_rate < 100:
        QTc = qt_interval / np.sqrt(rr_interval)
    else:
        QTc = qt_interval / (rr_interval ** (1/3))
    return QTc

# Streamlit应用
st.title("QTc计算器")
st.write("注意：当心率小于100时，将使用 Bazett 公式；当心率大于等于100时，将使用 Fridericia 公式。")

# 输入QT间期
qt_interval = st.number_input("输入QT间期（秒）：", min_value=0, value=400)
if qt_interval <= 0:
    st.error("QT间期必须大于0")
    st.stop()

# 输入心率
heart_rate = st.number_input("输入心率（次/min）：", min_value=1, value=75)
if heart_rate <= 0:
    st.error("心率必须大于0")
    st.stop()

# 根据心率计算RR间期
rr_interval = 60 / heart_rate

if st.button("计算QTc"):
    qtc_value = calculate_qtc(qt_interval, rr_interval, heart_rate)
    st.success(f"QTc值为：{qtc_value:.2f} 秒")
    st.write(f"计算所用的RR间期为：{rr_interval:.2f} 秒")
#读取数据
    
df=pd.read_excel('data/QT延长.xlsx')
st.write('有证据可延长QT间期的药物')
st.dataframe(df)
