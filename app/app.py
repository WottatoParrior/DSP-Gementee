import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from components.table.table import generate_table
from components.sidebar.sidebar import generate_sidebar
from components.datepicker.datepicker import generate_date_hour_picker

image_filename = "assets/MetroMap.svg"

app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
])

app.layout = generate_sidebar()


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            # html.H1('General stuff', style={'textAlign': 'center'}),
            generate_date_hour_picker(),
            html.Div(className="container",
                     children=[
                         html.Img(src=image_filename, className="metro-svg"),
                         html.Div(id="Centraal"),
                         html.Div(id="Spaklerweg"),
                         html.Div(id="VanDerMadeweg"),
                         html.Div(id="Zuid"),
                         html.Div(id="Bijlmer"),
                         html.Div(id="Strandvliet"),
                         html.Div(id="Duivendrecht"),
                     ])

            # dcc.Graph(id='bargraph',
            #           figure=px.bar(
            #               df,
            #               barmode='group',
            #               x='Years',
            #               y=['Girls Kindergarten', 'Boys Kindergarten']))
        ]
    elif pathname == "/venues":
        return [
            html.H1('Venues or smth', style={'textAlign': 'center'}),
        ]
    elif pathname == "/events":
        return [
            html.H1('Events', style={'textAlign': 'center'}),
            # dcc.Graph(id='bargraph',
            #           figure=px.bar(
            #               df,
            #               barmode='group',
            #               x='Years',
            #               y=['Girls High School', 'Boys High School']))
        ]
    elif pathname == "/stations":
        return [
            html.H1('Stations', style={'textAlign': 'center'}),
            # dcc.Graph(id='bargraph',
            #           figure=px.bar(
            #               df,
            #               barmode='group',
            #               x='Years',
            #               y=['Girls High School', 'Boys High School']))
        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)