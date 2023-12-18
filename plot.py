import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = pd.read_csv('./kbo_merge_data.csv')
data = data.astype({'Season': 'string'})

def make_plot(stat): 
    fig = make_subplots(
        rows= 2, cols= 3,
        subplot_titles=(f"{stat} X WAR", f"{stat} X wRC+", f"{stat} X ERA+", 
                        f"{stat} X SAVE", f"{stat} X RBI", f"{stat} X Lose")

    fig.add_trace(
        go.Scatter(x = data[stat], y = data["WAR"], mode='markers', marker=dict(size=3)),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["wRC+"], mode='markers', marker=dict(size=3)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["ERA+"], mode='markers', marker=dict(size=3)),
        row=1, col=3
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["SAVE"], mode='markers', marker=dict(size=3)),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["RBI"], mode='markers', marker=dict(size=3)),
        row=2, col=2
    )
    fig.add_trace(
        go.Scatter(x = data[stat], y = data["Lose"], mode='markers', marker=dict(size=3)),
        row=2, col=3
    )

    fig.update_yaxes(title_text="WAR", row=1, col=1)
    fig.update_yaxes(title_text="wRC+", row=1, col=2)
    fig.update_yaxes(title_text="ERA+", row=1, col=3)

    fig.update_yaxes(title_text="SAVE", row=2, col=1)
    fig.update_yaxes(title_text="RBI", row=2, col=2)
    fig.update_yaxes(title_text="Lose", row=2, col=3)



    fig.update_xaxes(title_text=stat, row=1, col=1)
    fig.update_xaxes(title_text=stat, row=1, col=2)
    fig.update_xaxes(title_text=stat, row=1, col=3)

    fig.update_xaxes(title_text=stat, row=2, col=1)
    fig.update_xaxes(title_text=stat, row=2, col=2)
    fig.update_xaxes(title_text=stat, row=2, col=3)

    

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
