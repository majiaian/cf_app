# app.py

import streamlit as st

st.set_page_config(page_title="药物辅助决策工具", layout="wide")

page1 = st.Page("pages/1_Antibio.py", title="抗菌药物")
page2 = st.Page("pages/2_PPI.py", title="PPI")
page3 = st.Page("pages/3_Albumin.py", title="人血白蛋白")
page4 = st.Page("pages/QTc.py", title="QTc计算")
page5 = st.Page("pages/CURB65.py", title="CURB65评分")
pages = {
    "辅助决策": [page1,page2,page3],
    "公式工具": [page4,page5],
}


pg = st.navigation(pages)
pg.run()