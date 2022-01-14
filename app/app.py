import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
df = pd.read_csv("../data/venues.csv")

image_filename = "assets/MetroMap.svg"

app = dash.Dash(__name__,
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                ],
                suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.H2("Amsterdam Mobility", className="display-6 head"),
            html.Hr(),
            html.P("Visualisations and stats", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Overview", href="/", active="exact"),
                    dbc.NavLink("Venues", href="/venues", active="exact"),
                    dbc.NavLink("Events", href="/events", active="exact"),
                    dbc.NavLink("Stations", href="/stations", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    ),
    html.Div(id="page-content", children=[], style=CONTENT_STYLE)
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            # html.H1('General stuff', style={'textAlign': 'center'}),
            html.Div([
                dcc.DatePickerSingle(date='2020-05-27',
                                     id="date-picker",
                                     display_format='MMM Do, YYYY'),
                dcc.Slider(id="hour-slider",
                           min=5,
                           max=24,
                           step=None,
                           marks={
                               5: '05:00',
                               6: '06:00',
                               7: '07:00',
                               8: '08:00',
                               9: '09:00',
                               10: '10:00',
                               11: '11:00',
                               12: '12:00',
                               13: '13:00',
                               14: '14:00',
                               15: '15:00',
                               16: '16:00',
                               17: '17:00',
                               18: '18:00',
                               19: '19:00',
                               20: '20:00',
                               21: '21:00',
                               22: '22:00',
                               23: '23:00',
                               24: '24:00',
                           },
                           value=5,
                           className="slider"),
            ], ),
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
                     ]),
            html.Div(
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
                                                  id="arena",
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
                                                  id="afas",
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
                                                  id="ziggo",
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
                                                  id="toekmost",
                                                  className="venue-numbers",
                                              ),
                                              html.H2(
                                                  "/2250",
                                                  className="venue-numbers",
                                              ),
                                          ]),
                             ]),
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


@app.callback(Output('arena', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    if selected_hour > 9:
        parsed_hour = selected_hour
    elif selected_hour == 24:
        parsed_hour = "0"
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)

    filtered_df = df[df["Time_to_filter"] == filter]
    return filtered_df["At_ArenA_beginning_of_hour"]


@app.callback(Output('toekmost', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    if selected_hour > 9:
        parsed_hour = selected_hour
    elif selected_hour == 24:
        parsed_hour = "0"
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)

    filtered_df = df[df["Time_to_filter"] == filter]
    return filtered_df["At_De_Toekmost_beginning_of_hour"]


@app.callback(Output('afas', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    if selected_hour > 9:
        parsed_hour = selected_hour
    elif selected_hour == 24:
        parsed_hour = "0"
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)

    filtered_df = df[df["Time_to_filter"] == filter]
    return filtered_df["At_AFAS_beginning_of_hour"]


@app.callback(Output('ziggo', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    if selected_hour > 9:
        parsed_hour = selected_hour
    elif selected_hour == 24:
        parsed_hour = "0"
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)

    filtered_df = df[df["Time_to_filter"] == filter]
    return filtered_df["At_Ziggo_beginning_of_hour"]


if __name__ == '__main__':

    app.run_server(debug=True, port=3000)