import streamlit as st

def calDY():
    col1, col2 = st.columns(2)
    with col1:
        zhengzhi = st.number_input(
            label="政治思想",
            min_value=0,
            max_value=15,
            value=0,
            step=1
        )
        faji = st.number_input(
            label='法纪观念',
            min_value=0,
            max_value=15,
            value=0,
            step=1
        )
        jiti = st.number_input(
            label='集体观念',
            min_value=0,
            max_value=15,
            value=0,
            step=1
        )
    with col2:
        daode = st.number_input(
            label="道德品质",
            min_value=0,
            max_value=15,
            value=0,
            step=1
        )
        xuexi = st.number_input(
            label='学习态度',
            min_value=0,
            max_value=15,
            value=0,
            step=1
        )
        wenhua = st.number_input(
            label='文化素养',
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

    anquan = st.number_input(
        label='安全卫生',
        min_value=0,
        max_value=15,
        value=0,
        step=1
    )
    total_points = zhengzhi + daode + faji + xuexi + jiti + wenhua + anquan
    if total_points < 60:
        flag = '不及格'
    elif total_points < 74:
        flag = '及格'
    elif total_points < 89:
        flag = '良好'
    elif total_points <= 100:
        flag = '优秀'
    st.write('你的德育基准分是:',total_points)
    st.write('你的德育等级是:',flag)

def calNL():
    col1, col2 = st.columns(2)
    with col1:
        nengli1 = st.number_input(
            label="社会工作能力",
            min_value=0,
            max_value=12,
            value=0,
            step=1
        )
        nengli2 = st.number_input(
            label='学科竞赛和科技竞赛',
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )
        nengli3 = st.number_input(
            label="学术科技成果",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )
    with col2:
        nengli4 = st.number_input(
            label='大学英语国家考试',
            min_value=0,
            max_value=18,
            value=0,
            step=1
        )
        nengli5 = st.number_input(
            label='计算机能力',
            min_value=0,
            max_value=30,
            value=0,
            step=1
        )
        nengli6 = st.number_input(
            label='文体比赛',
            min_value=0,
            max_value=50,
            value=0,
            step=1
        )
    nengli7 = st.number_input(
            label='国际化能力',
            min_value=0,
            max_value=50,
            value=0,
            step=1
        )

    total_nl = nengli1 + nengli2 + nengli3 + nengli4+nengli5+nengli6+nengli7
    st.write('你的能力基准分是', total_nl)

def calZY():
    jd = st.number_input(
        label="平均学分绩点",
        max_value=5.0,
        step=0.1,
    )
    total_point = (jd-1)*10+60
    st.write("你的智育基准分是",total_point)
if __name__ == '__main__':
    st.markdown('''
    ## 南邮综合素质评价计算
    ''')
    st.markdown('''
    ### 1. 德育
    ''')
    with st.expander("德育评分", expanded=False):
        calDY()
    st.markdown('''
    ### 2. 能力
    ''')
    with st.expander("能力评分",expanded=False):
        calNL()
    st.markdown('''
    ### 3.智育
''')
    with st.expander("智育评分",expanded=True):
        calZY()
