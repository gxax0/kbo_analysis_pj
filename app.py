import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 팀 예측 정보 DataFrame 생성
team_wins = pd.DataFrame({
    'Team': ['Kiwoom', 'Doosan', 'Samsung', 'NC', 'SSG', 'Hanhwa', 'KT', 'LG', 'Lotte', 'KIA'],
    'Win_predicted': [363.057465, 315.657867, 231.106201, 223.617065, 142.014801, 120.586334, 112.314529, 84.868568, 65.908394, 65.378014],
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

# 팀 성적 정보 DataFrame 생성
team_stats = pd.DataFrame({
    'Team': ['Kiwoom', 'Doosan', 'Samsung', 'NC', 'SSG', 'Hanhwa', 'KT', 'LG', 'Lotte', 'KIA'],
    'Batting_average': [0.294, 0.285, 0.278, 0.267, 0.262, 0.255, 0.252, 0.249, 0.242, 0.235],
    'Home_runs': [200, 185, 173, 157, 148, 140, 137, 135, 126, 121],
    'Stolen_bases': [88, 84, 81, 69, 66, 63, 60, 59, 57, 55]
})

# Streamlit 앱 시작
st.header('⚾ KBO 한국 프로야구 우승팀 예측 모델 📈')
st.markdown("""---""")

def main():
    st.title('팀 순위 & 성적 비교')

    # 팀 선택
    team1 = st.selectbox('팀 1을 선택하세요:', team_wins['Team'])
    team2 = st.selectbox('팀 2를 선택하세요:', team_wins['Team'])

    # 선택한 팀 이외의 팀들 제거
    filtered_teams = team_wins[(team_wins['Team'] == team1) | (team_wins['Team'] == team2)]

    # 순위 비교 함수
    def compare_rank(team1, team2):
        rank1 = filtered_teams[filtered_teams['Team'] == team1]['Rank'].values[0]
        rank2 = filtered_teams[filtered_teams['Team'] == team2]['Rank'].values[0]

        if rank1 < rank2:
            return f'{team1}가 {team2}보다 높은 순위입니다.'
        elif rank1 > rank2:
            return f'{team2}가 {team1}보다 높은 순위입니다.'
        else:
            return f'{team1}과 {team2}의 순위가 동일합니다.'

    # 성적 비교 함수
    def compare_stats(team1, team2):
        stats1 = team_stats[team_stats['Team'] == team1].iloc[0]
        stats2 = team_stats[team_stats['Team'] == team2].iloc[0]

        comparison = pd.DataFrame({
            '지표': ['타율', '홈런', '도루'],
            team1: [stats1['Batting_average'], stats1['Home_runs'], stats1['Stolen_bases']],
            team2: [stats2['Batting_average'], stats2['Home_runs'], stats2['Stolen_bases']]
        })

        return comparison.set_index('지표')

    # 순위 비교 및 결과 출력
    result = compare_rank(team1, team2)
    st.write(result)

    # 성적 비교 및 결과 출력
    st.write('## 성적 비교')
    st.write(compare_stats(team1, team2))

    # 그래프 생성 및 설정
    fig, ax = plt.subplots()
    comparison = compare_stats(team1, team2)
    comparison.plot(kind='bar', ax=ax)
    ax.set_xlabel('지표')
    ax.set_ylabel('값')
    ax.set_title('팀 성적 비교')

    # 한글 글꼴 경로 설정
    font_path = r'C:\Users\PC\PycharmProjects\pythonProject\sejong_ttf\Sejong hospital Light.ttf'
    fontprop = fm.FontProperties(fname=font_path)

    # 그래프에 한글 글꼴 적용
    plt.rcParams['font.family'] = fontprop.get_name()

    st.pyplot(fig)

if __name__ == '__main__':
    main()
