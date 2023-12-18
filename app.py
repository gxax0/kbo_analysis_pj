
import streamlit as st
import seaborn as sns
import pandas as pd
 

# st.title('')
st.header('⚾ KBO 한국 프로야구 우승팀 예측 모델 📈')
st.markdown("""---""")
data = pd.read_csv('./kbo_merge_data.csv')

# Seaborn correlation plot 생성
plot = sns.heatmap(df.corr(), annot=True)
 
# 플롯을 Streamlit에 표시
st.pyplot(plot.get_figure())
