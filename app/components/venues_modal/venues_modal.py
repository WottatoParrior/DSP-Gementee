from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("../data/venues.csv")


def generate_venues_modal():
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
                                          "Number",
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
                                          "Number",
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
                                          "Number",
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
                                          "Number",
                                          className="venue-numbers",
                                      ),
                                      html.H2(
                                          "/2250",
                                          className="venue-numbers",
                                      ),
                                  ]),
                     ]),
        ])
