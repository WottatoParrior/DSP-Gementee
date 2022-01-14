from dash import dcc, html
from app import app
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv("../data/venues.csv")


@app.callback(Output('graph-with-slider', 'figure'),
              Input('hour-slider', 'value'))
def update_venues(selected_hour):
    print(selected_hour)
    return selected_hour


def generate_venues_modal(values):
    return html.Div(
        className="venues-modal",
        children=[
            # html.Img(src=, className="metro-svg"),
            html.H2("Venues",
                    className="head",
                    style={"padding": "0px 0px 10px 10px"}),
            html.Div(className="venue-container",
                     children=[
                         html.Div(className="venue",
                                  children=[
                                      html.H2(
                                          "ArenA",
                                          className="venue-name",
                                      ),
                                      html.H2(
                                          values[0],
                                          className="venue-numbers",
                                      ),
                                      html.H2(
                                          "/54900",
                                          className="venue-numbers",
                                      ),
                                  ]),
                         html.Div(className="venue",
                                  children=[
                                      html.H2(
                                          "AFAS",
                                          className="venue-name",
                                      ),
                                      html.H2(
                                          values[1],
                                          className="venue-numbers",
                                      ),
                                      html.H2(
                                          "/6000",
                                          className="venue-numbers",
                                      ),
                                  ]),
                         html.Div(className="venue",
                                  children=[
                                      html.H2(
                                          "Ziggo Dome",
                                          className="venue-name",
                                      ),
                                      html.H2(
                                          values[2],
                                          className="venue-numbers",
                                      ),
                                      html.H2(
                                          "/17000",
                                          className="venue-numbers",
                                      ),
                                  ]),
                         html.Div(className="venue",
                                  children=[
                                      html.H2(
                                          "De Toekmost",
                                          className="venue-name",
                                      ),
                                      html.H2(
                                          values[3],
                                          className="venue-numbers",
                                      ),
                                      html.H2(
                                          "/2250",
                                          className="venue-numbers",
                                      ),
                                  ]),
                     ]),
        ])
