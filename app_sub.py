import streamlit as st
import pandas as pd
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

st.header('⚾ KBO 한국 프로야구 우승팀 예측 모델 📈')
st.markdown("""---""")
df = pd.read_csv('./kbo_merge_data.csv')

# seaborn pairplot 생성
plot = sns.pairplot(df)

# plot을 streamlit에 표시
st.pyplot(plot)

# 피처 선택
features = ['ERA+', 'Save', 'WAR', 'Lose']
X = df[features]
y = df['Win']

# 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost 회귀 모델 생성
model = XGBRegressor()

# 모델 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 팀 이름과 예측 승수 설정
team_wins = pd.DataFrame({'Team': df['Team'][X_test.index], 'Win_predicted': y_pred})

# 그래프 사이즈 설정
plt.figure(figsize=(10, 8))

# 바 차트 생성
plt.barh(team_wins['Team'], team_wins['Win_predicted'], color='skyblue')

# 그래프 제목 및 x, y 레이블 설정
plt.title('Team Winning Prediction')
plt.xlabel('Predicted Wins')
plt.ylabel('Team')

# y축의 순서를 높은 순위가 위로 오도록 변경
plt.gca().invert_yaxis()

# Streamlit에 Matplotlib 그림 표시
st.pyplot(plt)
