import streamlit as st

def calDY():
    col1, col2 = st.columns(2)
    with col1:
        zhengzhi = st.number_input(
            label="政治思想",
            min_value=0,
            max_value=15,
            step=1,
            value=0
        )
        faji = st.number_input(
            label='法纪观念',
            min_value=0,
            max_value=15,
            step=1,
            value=0
        )
        jiti = st.number_input(
            label='集体观念',
            min_value=0,
            max_value=15,
            step=1,
            value=0
        )
    with col2:
        daode = st.number_input(
            label="道德品质",
            min_value=0,
            max_value=15,
            step=1,
            value=0
        )
        xuexi = st.number_input(
            label='学习态度',
            min_value=0,
            max_value=15,
            step=1,
            value=0
        )
        wenhua = st.number_input(
            label='文化素养',
            min_value=0,
            max_value=10,
            step=1,
            value=0
        )

    anquan = st.number_input(
        label='安全卫生',
        min_value=0,
        max_value=15,
        step=1,
        value=0
    )
    dy_top = st.number_input(
        label='本班德育最高分',
        min_value=1,
        max_value=100,
        step=1,
        value=100
    )

    total_points = zhengzhi + daode + faji + xuexi + jiti + wenhua + anquan

    if total_points > 0:
        if total_points < 60:
            flag = '不及格'
        elif total_points < 74:
            flag = '及格'
        elif total_points < 89:
            flag = '良好'
        elif total_points <= 100:
            flag = '优秀'

        dy_end = (total_points / dy_top) * 15
        st.write('你的德育基准分是:', total_points)
        st.write('你的德育等级是:', flag)
        st.write('德育加权分是：', dy_end)
        return dy_end
    else:
        return 0

def calNL():
    col1, col2 = st.columns(2)
    with col1:
        nengli1 = st.number_input(
            label="社会工作能力",
            min_value=0,
            max_value=12,
            step=1,
            value=0
        )
        nengli2 = st.number_input(
            label='学科竞赛和科技竞赛',
            min_value=0,
            max_value=100,
            step=1,
            value=0
        )
        nengli3 = st.number_input(
            label="学术科技成果",
            min_value=0,
            max_value=100,
            step=1,
            value=0
        )
    with col2:
        nengli4 = st.number_input(
            label='大学英语国家考试',
            min_value=0,
            max_value=18,
            step=1,
            value=0
        )
        nengli5 = st.number_input(
            label='计算机能力',
            min_value=0,
            max_value=30,
            step=1,
            value=0
        )
        nengli6 = st.number_input(
            label='文体比赛',
            min_value=0,
            max_value=50,
            step=1,
            value=0
        )
    nengli7 = st.number_input(
            label='国际化能力',
            min_value=0,
            max_value=50,
            step=1,
            value=0
        )
    nl_top = st.number_input(
        label="本专业能力最高分",
        min_value=1,
        max_value=100,
        step=1,
        value=100
    )

    total_nl = nengli1 + nengli2 + nengli3 + nengli4 + nengli5 + nengli6 + nengli7

    if total_nl > 0:
        nl_end = (total_nl / nl_top) * 15
        st.write('你的能力基准分是', total_nl)
        st.write('你的能力加权分是：', nl_end)
        return nl_end
    else:
        return 0

def calZY():
    jd = st.number_input(
        label="平均学分绩点",
        min_value=0.0,
        max_value=5.0,
        step=0.1,
        value=0.0
    )
    jd_top = st.number_input(
        label="本专业绩点最高分",
        min_value=1.0,
        max_value=5.0,
        step=0.1,
        value=5.0
    )

    if jd > 0:
        total_point = (jd - 1) * 10 + 60
        jd_end = (total_point / jd_top) * 70
        st.write("你的智育基准分是", total_point)
        st.write("你的智育加权分是", jd_end)
        return jd_end
    else:
        return 0

if __name__ == '__main__':
    st.markdown('''
    ## 南邮综合素质评价计算
    ''')
    st.markdown('''
    ### 1. 德育
    ''')
    with st.expander("德育评分", expanded=False):
        dy_end = calDY()
    st.markdown('''
    ### 2. 能力
    ''')
    with st.expander("能力评分", expanded=False):
        nl_end = calNL()
    st.markdown('''
    ### 3. 智育
    ''')
    with st.expander("智育评分", expanded=True):
        jd_end = calZY()

    st.markdown('''
    ### 你的综测总分是
    ''')
    total_score = dy_end + nl_end + jd_end
    if total_score !=0:
        st.metric(total_score)
