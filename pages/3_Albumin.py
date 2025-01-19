import streamlit as st

def display_hepatocirrhosis_advice():
    st.subheader("肝硬化使用")
    st.write("决策图如下图")
    st.image("images/白蛋白/肝硬化.png")
    
    
def display_hypovolemia_advice():
    st.subheader("血容量不足使用")
    st.write("决策图如下图")
    st.image("images/白蛋白/血容量不足.png")
    
option = st.radio("白蛋白使用场景", ["肝硬化使用", "血容量不足使用"])

if option == "肝硬化使用":
    display_hepatocirrhosis_advice()
elif option == "血容量不足使用":
    display_hypovolemia_advice()
    
