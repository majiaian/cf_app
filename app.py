# app.py

import streamlit as st

page1 = st.Page("pages/1_Antibio.py", title="抗菌药物")
page2 = st.Page("pages/2_PPI.py", title="PPI")
page3 = st.Page("pages/3_Albumin.py", title="人血白蛋白")
pages = {
    "辅助决策": [page1, page2，page3],
    "公式工具": [],
}


pg = st.navigation(pages)
pg.run()