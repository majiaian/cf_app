# app.py

import streamlit as st

st.set_page_config(page_title="药物辅助决策工具",initial_sidebar_state="expanded")

page1 = st.Page("pages/1_Antibio.py", title="抗菌药物")
page2 = st.Page("pages/2_PPI.py", title="PPI")
page3 = st.Page("pages/3_Albumin.py", title="人血白蛋白")
page4 = st.Page("pages/5_QTc.py",title="QTc计算")
page5 = st.Page("pages/6_CURB65.py", title="CURB65肺炎评分")
page6 = st.Page("pages/4_OPTCAD.py", title="OPTCAD心肌缺血评分")
page7 = st.Page("pages/7_LRINEC.py", title="LRINEC坏死性筋膜炎评分")
pages = {
    "辅助决策": [page1,page2,page3],
    "公式工具": [page4,page5,page6,page7],
}


pg = st.navigation(pages)
pg.run()
