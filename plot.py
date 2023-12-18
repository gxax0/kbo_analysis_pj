import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = pd.read_csv('./data.csv')
data = data.astype({'연도': 'string'})

def make_plot(stat): 
    fig = make_subplots(
        rows= 6, cols= 3,
        subplot_titles=(f"{stat} X 타율", f"{stat} X 출루", f"{stat} X 장타", 
                        f"{stat} X OPS", f"{stat} X 경기당득점", f"{stat} X 경기당안타", 
                        f"{stat} X 경기당2루타", f"{stat} X 경기당3루타", f"{stat} X 경기당홈런", 
                        f"{stat} X 경기당루타", f"{stat} X 경기당타점", f"{stat} X 경기당도루",
                        f"{stat} X 경기당볼넷", f"{stat} X 경기당삼진", f"{stat} X 경기당병살", 
                        f"{stat} X 경기당희생타"))

    fig.add_trace(
        go.Scatter(x = data[stat], y = data["타율"], mode='markers', marker=dict(size=3)),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["출루"], mode='markers', marker=dict(size=3)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["장타"], mode='markers', marker=dict(size=3)),
        row=1, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["OPS"], mode='markers', marker=dict(size=3)),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당득점"], mode='markers', marker=dict(size=3)),
        row=2, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당안타"], mode='markers', marker=dict(size=3)),
        row=2, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당2루타"], mode='markers', marker=dict(size=3)),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당3루타"], mode='markers', marker=dict(size=3)),
        row=3, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당홈런"], mode='markers', marker=dict(size=3)),
        row=3, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당루타"], mode='markers', marker=dict(size=3)),
        row=4, col=1
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당타점"], mode='markers', marker=dict(size=3)),
        row=4, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당도루"], mode='markers', marker=dict(size=3)),
        row=4, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당볼넷"], mode='markers', marker=dict(size=3)),
        row=5, col=1
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당삼진"], mode='markers', marker=dict(size=3)),
        row=5, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당병살"], mode='markers', marker=dict(size=3)),
        row=5, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["경기당희생타"], mode='markers', marker=dict(size=3)),
        row=6, col=1
    )

    fig.update_yaxes(title_text="타율", row=1, col=1)
    fig.update_yaxes(title_text="출루", row=1, col=2)
    fig.update_yaxes(title_text="장타", row=1, col=3)

    fig.update_yaxes(title_text="OPS", row=2, col=1)
    fig.update_yaxes(title_text="경기당득점", row=2, col=2)
    fig.update_yaxes(title_text="경기당안타", row=2, col=3)

    fig.update_yaxes(title_text="경기당2루타", row=3, col=1)
    fig.update_yaxes(title_text="경기당3루타", row=3, col=2)
    fig.update_yaxes(title_text="경기당홈런", row=3, col=3)

    fig.update_yaxes(title_text="경기당루타", row=4, col=1)
    fig.update_yaxes(title_text="경기당타점", row=4, col=2)
    fig.update_yaxes(title_text="경기당도루", row=4, col=3)

    fig.update_yaxes(title_text="경기당볼넷", row=5, col=1)
    fig.update_yaxes(title_text="경기당삼진", row=5, col=2)
    fig.update_yaxes(title_text="경기당병살", row=5, col=3)

    fig.update_yaxes(title_text="경기당희생타", row=6, col=1)



    fig.update_xaxes(title_text=stat, row=1, col=1)
    fig.update_xaxes(title_text=stat, row=1, col=2)
    fig.update_xaxes(title_text=stat, row=1, col=3)

    fig.update_xaxes(title_text=stat, row=2, col=1)
    fig.update_xaxes(title_text=stat, row=2, col=2)
    fig.update_xaxes(title_text=stat, row=2, col=3)

    fig.update_xaxes(title_text=stat, row=3, col=1)
    fig.update_xaxes(title_text=stat, row=3, col=2)
    fig.update_xaxes(title_text=stat, row=3, col=3)

    fig.update_xaxes(title_text=stat, row=4, col=1)
    fig.update_xaxes(title_text=stat, row=4, col=2)
    fig.update_xaxes(title_text=stat, row=4, col=3)

    fig.update_xaxes(title_text=stat, row=5, col=1)
    fig.update_xaxes(title_text=stat, row=5, col=2)
    fig.update_xaxes(title_text=stat, row=5, col=3)

    fig.update_xaxes(title_text=stat, row=6, col=1)

    fig.update_layout(
        width = 800, height = 1800,
        showlegend=False,
        # plot_bgcolor = '#161A1D',
        # paper_bgcolor = '#161A1D',
        font_color = '#FFFFFF'
    )
    fig.update_yaxes(gridcolor = '#687B8A')
    fig.update_xaxes(gridcolor = '#687B8A')
    return fig


    # fig.update_layout({
    # ‘plot_bgcolor’: ‘rgba(0, 0, 0, 0)’,
    # ‘paper_bgcolor’: ‘rgba(0, 0, 0, 0)’,
    # })

def make_plot2(stat):
    tmp = pd.DataFrame(data.iloc[:,2:].corr(method='pearson')[stat])
    fig = px.imshow(tmp.sort_values(by=stat, ascending=False), text_auto=True, aspect="auto", color_continuous_scale='Blues')
    fig.update_layout(height=1000, width=300)

    return fig
