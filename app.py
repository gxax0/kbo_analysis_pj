import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# st.title('')
st.header('⚾ KBO 한국 프로야구 우승팀 예측 모델 📈')
st.markdown("""---""")
df = pd.read_csv('./kbo_merge_data.csv')


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
# 팀 이름과 예측 승수를 x, y로 설정
x = team_wins['Team']
y = team_wins['Win_predicted']

# 그래프 사이즈 설정
plt.figure(figsize=(10, 8))

# 바 차트 생성
plt.barh(x, y, color='skyblue')

# 그래프 제목 및 x, y 레이블 설정
plt.title('Team Winning Prediction')
plt.xlabel('Predicted Wins')
plt.ylabel('Team')

# y축의 순서를 높은 순위가 위로 오도록 변경
plt.gca().invert_yaxis()

# 그래프 보여주기
plt.show()
