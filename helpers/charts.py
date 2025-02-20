import pandas as pd
import plotly.express as px
import streamlit as st

from helpers.processing import *

def plot_time_series(raw_df, ownership, year_start, year_end, companies, metric, type_rep, industries):
    metric_en = get_metrics().loc[get_metrics()['code'] == metric, 'name'].values[0]

    # Filter data
    if type_rep:
        df = raw_df[(raw_df['Accper_year'] >= year_start) & (raw_df['Accper_year'] <= year_end) & (raw_df['Typrep'] == type_rep) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['final_company_name'].isin(companies)) & (raw_df['ownership'].isin(ownership))]
    else:
        df = raw_df[(raw_df['Accper_year'] >= year_start) & (raw_df['Accper_year'] <= year_end) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['final_company_name'].isin(companies)) & (raw_df['ownership'].isin(ownership))]
 
    fig = px.line(df, x='Accper_year', y=metric, color='final_company_name', title=metric_en)

    # Add labels to the axes
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text=metric_en)

    # Move legend to the bottom
    fig.update_layout(showlegend=False)

    return fig

def scatterplot_one_metric(raw_df, index, year, companies, metric_1, type_rep, industries, ownership):
    metric_en = get_metrics().loc[get_metrics()['code'] == metric_1, 'name'].values[0]

    # Filter data
    if type_rep:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['Typrep'] == type_rep) & (raw_df['final_company_name'].isin(companies)) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]
    else:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['final_company_name'].isin(companies)) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]
    
    # Calculate average values for Metric 1 and Metric 2
    avg_metric_1 = df[metric_1].mean()

    # Create a scatter plot using Plotly
    fig = px.scatter(df, x='final_company_name', y=metric_1, text='final_company_name' if len(companies) < 11 else None, custom_data=["final_company_name"], title=f"Scatter plot of {index} index companies on {metric_en} in year {year}", color='Indnme_En')

    # Customize the plot (optional)
    fig.update_traces(textposition="top center", marker=dict(size=4 if len(companies) > 30 else 10, opacity=0.8))

    # Add labels to the axes
    fig.update_xaxes(showticklabels=False, title_text="")
    fig.update_yaxes(title_text=metric_en)

    # Add market average lines
    fig.add_shape(type='line',
                x0=-0.5, y0=avg_metric_1,
                x1=len(df['Stkcd'].unique()) * 1.05, y1=avg_metric_1,
                line=dict(color="red", width=1))

    fig.add_annotation(
        x=len(df['Stkcd'].unique()) * 1.05, y=avg_metric_1,
        text=f'Avg: {round(avg_metric_1,4)}',
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        arrowwidth=2,
        bordercolor="black",
        borderwidth=2,
        bgcolor="white"
    )

    # Move legend to the bottom
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.4 if len(df['Indnme_En'].unique()) < 30 else -10.0, xanchor="left", x=0))

    fig.update_layout(showlegend=True, legend_title_text="Industry")
    fig.update_layout(height=1000)
    # Show the plot
    return fig, df

def scatterplot_two_metrics(raw_df, index, year, metric_1, metric_2, type_rep, companies, industries, ownership):
    metric_one_en = get_metrics().loc[get_metrics()['code'] == metric_1, 'name'].values[0]
    metric_two_en = get_metrics().loc[get_metrics()['code'] == metric_2, 'name'].values[0]

    # Filter data
    if type_rep:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['Typrep'] == type_rep) & (raw_df['final_company_name'].isin(companies)) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]
    else:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['final_company_name'].isin(companies)) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]
    # Calculate average values for Metric 1 and Metric 2
    avg_metric_1 = df[metric_1].mean()
    avg_metric_2 = df[metric_2].mean()

    # Create a scatter plot using Plotly
    fig = px.scatter(df, x=metric_1, y=metric_2, text='final_company_name' if len(companies) < 11 else None, custom_data=["final_company_name"], title=f"Scatter plot of {index} index companies on {metric_one_en} and {metric_two_en} in {year}", color='Indnme_En')

    # Customize the plot (optional)
    fig.update_traces(textposition="top center", marker=dict(size=4 if len(companies) > 30 else 10, opacity=0.8))

    # Add labels to the axes
    fig.update_xaxes(title_text=metric_one_en, side='top')
    fig.update_yaxes(title_text=metric_two_en)

    # Add market average lines
    fig.add_shape(type='line',
                x0=avg_metric_1, y0=df[metric_2].min(),
                x1=avg_metric_1, y1=df[metric_2].max(),
                line=dict(color="red", width=1))

    fig.add_shape(type='line',
                x0=df[metric_1].min(), y0=avg_metric_2,
                x1=df[metric_1].max(), y1=avg_metric_2,
                line=dict(color="blue", width=1))

    fig.add_annotation(
        x=avg_metric_1, y=df[metric_2].max(),
        text=f'{metric_one_en} Avg: {round(avg_metric_1, 4)}',
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        arrowwidth=2,
        bordercolor="black",
        borderwidth=2,
        bgcolor="white"
    )

    fig.add_annotation(
        x=df[metric_1].max(), y=avg_metric_2,
        text=f'{metric_two_en} Avg: {round(avg_metric_2, 4)}',
        showarrow=True,
        arrowhead=2,
        arrowcolor="blue",
        arrowwidth=2,
        bordercolor="black",
        borderwidth=2,
        bgcolor="white"
    )

    # Move legend to the bottom
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.4 if len(df['Indnme_En'].unique()) < 30 else -3.0, xanchor="left", x=0))

    fig.update_layout(showlegend=True, legend_title_text="Industry")

    fig.update_layout(margin=dict(t=150))
    fig.update_layout(height=1000)

    # Show the plot
    return fig, df

def get_top_stocks(raw_df, number_to_display, metric, type_rep, year, industries, ownership):
    # Filter data
    if type_rep:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['Typrep'] == type_rep) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]
    else:
        df = raw_df[(raw_df['Accper_year'] == year) & (raw_df['Indnme_En'].isin(industries)) & (raw_df['ownership'].isin(ownership))]

    result_df = df.sort_values(by=metric, ascending=False).head(number_to_display).reset_index(drop=True)[['final_company_name', 'Indnme_En', 'ownership', 'F050201B', 'F051501B', 'F050501B', 'F010201A', 'F010101A', 'F011701A', 'F090101B', 'F100401A', 'F100101B']]

    return result_df.rename(columns={
        'final_company_name': 'Company',
        'Indnme_En': 'Industry',
        'ownership': 'Ownership Type',
        'F050201B': get_metrics_dict()['F050201B'],
        'F051501B': get_metrics_dict()['F051501B'],
        'F050501B': get_metrics_dict()['F050501B'],
        'F010201A': get_metrics_dict()['F010201A'],
        'F010101A': get_metrics_dict()['F010101A'],
        'F011701A': get_metrics_dict()['F011701A'],
        'F090101B': get_metrics_dict()['F090101B'],
        'F100401A': get_metrics_dict()['F100401A'],
        'F100101B': get_metrics_dict()['F100101B'],
    })