import streamlit as st

# 设置页面标题
st.header("抗菌药物使用")

# 定义抗菌药物使用的预防逻辑
def display_prevention_advice():
    st.subheader("围手术期预防")
    incision_type = st.selectbox("选择切口类别", ["一类切口（如永久起搏器）", "特殊诊疗操作（如先心病封堵、消融、7天内第二次造影）"])

    if incision_type == "一类切口（如永久起搏器）":
        st.write("用药建议：")
        st.write("头孢唑林1-2g q12h或头孢呋辛1.5g q12h，头孢过敏则克林霉素0.6g q12h或万古霉素1g q12h，预防疗程1-2d")
    elif incision_type == "特殊诊疗操作（如先心病封堵、消融、7天内第二次造影）":
        st.write("用药建议：")
        st.write("头孢唑林1-2g st或头孢呋辛1.5g st，头孢过敏则克林霉素0.6g st或万古霉素1g st")

# 定义抗菌药物使用的初始治疗逻辑
def display_initial_treatment_advice():
    st.subheader("初始治疗经验用药")
    st.write("上呼吸道感染多为病毒引起\n军团菌、鹦鹉热等非典型病原体检测手段不足，关注聚集发病、旅行史、鸟禽接触史等线索")
    st.write("肾功能不全剂量调整参考https://mp.weixin.qq.com/s/5kipswjJ4fU5cK0ob2LfDw")
    infection_site = st.selectbox("选择感染部位", ["肺部感染", "泌尿系感染", "感染性休克"])
    if infection_site == "肺部感染":
        infection_type = st.selectbox("选择感染类型", ["社区感染", "院内感染"])
        if infection_type == "社区感染":
            is_smoking_or_copd = st.selectbox("是否长期吸烟或支扩或COPD", ["是", "否"])
            if is_smoking_or_copd == "是":
                st.write("用药建议：")
                st.write("喹诺酮类（莫西除外）或者含酶抑制剂类药物±大环内酯类")
            elif is_smoking_or_copd == "否":
                is_elderly_or_recent_hospitalization = st.selectbox("是否老年或近期多次住院", ["是", "否"])
                if is_elderly_or_recent_hospitalization == "是":
                    st.write("用药建议：")
                    st.write("含酶抑制剂类药物±大环内酯类")
                else:
                    st.write("用药建议：")
                    st.write("三代头孢（他啶除外）±大环内酯类")        
        elif infection_type == "院内感染":
            st.write("用药建议：")
            st.write("含酶抑制剂类药物或碳青霉烯类")
    

    elif infection_site == "泌尿系感染":
        urinary_infection_type = st.selectbox("选择泌尿系感染类型", ["单纯下尿路感染", "其他"])
        if urinary_infection_type == "单纯下尿路感染":
            st.write("用药建议：")
            st.write("口服阿莫西林克拉维酸1g q12h或呋喃妥因1g q12h或磷霉素氨丁三醇3g st")
        else:  # 其他
            st.write("用药建议：")
            st.write("可结合既往用药史，分离病原体耐药情况，按头孢他啶--哌拉西林他唑巴坦--碳青霉烯类逐步升级")

    elif infection_site == "感染性休克":
        st.write("用药建议：")
        st.write("碳青霉烯类，有呼吸道症状加用大环内酯类或喹诺酮类")


option = st.radio("选择抗菌药物使用场景", ["围手术期预防", "初始治疗用药"])

if option == "围手术期预防":
    display_prevention_advice()
elif option == "初始治疗用药":
    display_initial_treatment_advice()


