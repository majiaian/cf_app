import streamlit as st

def display_prevention_advice():
    st.subheader("预防使用")
    incision_type = st.selectbox("选择预防使用场景", ["应激性溃疡", "药物相关性溃疡"])
    if incision_type == "应激性溃疡":
        st.write("适应症参考下图")
        st.image("images/ppis/预防应激性溃疡.png")
    elif incision_type == "药物相关性溃疡":
        st.write("使用抗血小板药物参考下图")
        st.image("images/ppis/抗血小板.png")
        st.write("使用非甾体抗炎药参考下图")
        st.image("images/ppis/NSAIDs.png")
    
def display_treatment_advice():
    st.subheader("治疗使用")
    st.write("适应症参考下图")
    st.image("images/ppis/治疗性使用.png")
    
option = st.radio("PPI使用场景", ["预防使用", "治疗使用"])

if option == "预防使用":
    display_prevention_advice()
elif option == "治疗使用":
    display_treatment_advice()
    
st.write("用药剂量参考下图")
st.image("images/ppis/剂量.png")