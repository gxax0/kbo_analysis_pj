import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plot as pl 

# st.title('')
st.header('⚾ KBO 한국 프로야구 우승팀 예측 모델 📈')
st.markdown("""---""")
data = pd.read_csv('./kbo_merge_data.csv')
data = data.astype({'Season': 'string'})

select_stat = st.selectbox(
    '궁금한 스탯을 고르세요.',
    data.iloc[:,2:].columns.tolist()
)

maxi = data.sort_values(by=select_stat, ascending=False).iloc[:3,:][select_stat].tolist()
year = data.sort_values(by=select_stat, ascending=False).iloc[:3,1].tolist()
team = data.sort_values(by=select_stat, ascending=False).iloc[:3,0].tolist()

st.write("  ")
st.write("  ")
st.write("  ")

tab1, tab2, tab3 = st.tabs(["우승 요소별 top3 팀🏆", "상관관계📈", "상관계수📊"])

with tab1:
    st.markdown(f'#### \'{select_stat}\'이(가) 가장 높았던 팀 3개를 알려드릴게요.')
    st.write("  ")
    st.markdown(f'##### 🥇 {year[0]}년 {team[0]}: {maxi[0]}')
    st.markdown(f'##### 🥈 {year[1]}년 {team[1]}: {maxi[1]}')
    st.markdown(f'##### 🥉 {year[2]}년 {team[2]}: {maxi[2]}')

with tab2:
    st.markdown(f'#### \'{select_stat}\'와(과) 다른 지표와의 상관관계를 나타낸 시각자료에요.')
    st.plotly_chart(pl.make_plot(select_stat))

with tab3:
    st.markdown(f'#### \'{select_stat}\'와(과) 다른 지표와의 상관계수를 큰 순서대로 나타냈어요.')
    st.markdown(f'※ pearson 상관계수 기준')
    st.plotly_chart(pl.make_plot2(select_stat))
