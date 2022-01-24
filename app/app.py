import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from helpers.helpers import create_filter_venues, create_filter_stations, create_hover_info
import plotly.graph_objects as go

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

# stations_capacity = [
#     50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750,
#     800, 850
# ]
# stations_capacity_figure = go.Figure()

# stations_capacity_figure.add_trace(
#     go.Scatter(
#         x=[72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112],
#         y=stations_capacity,
#         marker=dict(color="crimson", size=12),
#         mode="markers",
#         name="Women",
#     ))

# stations_capacity_figure.add_trace(
#     go.Scatter(
#         x=[
#             92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151,
#             152, 165
#         ],
#         y=stations_capacity,
#         marker=dict(color="gold", size=12),
#         mode="markers",
#         name="Men",
#     ))

# stations_capacity_figure.update_layout(
#     title="Gender Earnings Disparity",
#     xaxis_title="Annual Salary (in thousands)",
#     yaxis_title="School")

df_venues = pd.read_csv("../data/venues.csv")
df_events = pd.read_csv("../data/events.csv")
df_events_schedule = pd.read_csv("../data/events_to_display.csv")

image_filename = "assets/metro.jpg"

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
            html.Div([
                dcc.DatePickerSingle(date='2020-05-27',
                                     id="date-picker",
                                     display_format='MMM Do, YYYY'),
                dcc.Slider(id="hour-slider",
                           min=0,
                           max=23,
                           step=None,
                           marks={
                               0: "00:00",
                               1: '01:00',
                               2: '02:00',
                               3: '03:00',
                               4: '04:00',
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
                           },
                           value=5,
                           className="slider"),
            ], ),
            html.Div(
                className="container",
                children=[
                    html.Img(src=image_filename, className="metro-svg"),
                    html.Div(id="Centraal-info", className="info-hover"),
                    html.Div(id="Centraal", className="station"),
                    #------------------------------------------#
                    html.Div(id="Spaklerweg-info", className="info-hover"),
                    html.Div(id="Spaklerweg", className="station"),
                    #------------------------------------------#
                    html.Div(id="VanDerMadeweg-info", className="info-hover"),
                    html.Div(id="VanDerMadeweg", className="station"),
                    #------------------------------------------#
                    html.Div(id="Zuid-info", className="info-hover"),
                    html.Div(id="Zuid", className="station"),
                    #------------------------------------------#
                    html.Div(id="Bijlmer-info", className="info-hover"),
                    html.Div(id="Bijlmer", className="station"),
                    #------------------------------------------#
                    html.Div(id="Strandvliet-info", className="info-hover"),
                    html.Div(id="Strandvliet", className="station"),
                    #------------------------------------------#
                    html.Div(id="Duivendrecht-info", className="info-hover"),
                    html.Div(id="Duivendrecht", className="station"),
                    #------------------------------------------#
                    html.Div(id="NS-info", className="info-hover"),
                    html.Div(id="NS", className="station"),
                    #------------------------------------------#
                    html.Div(id="NA-info", className="info-hover"),
                    html.Div(id="NA", className="station"),
                    #------------------------------------------#
                    html.Div(id="VG-info", className="info-hover"),
                    html.Div(id="VG", className="station"),
                    #------------------------------------------#
                    html.Div(id="BG-info", className="info-hover"),
                    html.Div(id="BG", className="station"),
                    #------------------------------------------#
                    html.Div(id="IA-info", className="info-hover"),
                    html.Div(id="IA", className="station"),
                    #------------------------------------------#
                    html.Div(id="RE-info", className="info-hover"),
                    html.Div(id="RE", className="station"),
                    #------------------------------------------#
                    html.Div(id="RO-info", className="info-hover"),
                    html.Div(id="RO", className="station"),
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
                ]),
            html.Div(
                className="events-modal",
                children=[
                    # html.Img(src=, className="metro-svg"),
                    html.H2("Events",
                            className="head",
                            style={"padding": "0px 0px 10px 10px"}),
                    html.Div(className="event-container", id="events"),
                ]),
            html.Div(
                className="color-helper",
                children=[
                    # html.Img(src=, className="metro-svg"),
                    html.Div("No color", className="color-item"),
                    html.Div("Less than regular crowdness",
                             className="color-item"),
                    html.Div(className="color-item green"),
                    html.Div("0%-30% Increased crowdness",
                             className="color-item"),
                    html.Div(className="color-item"),
                    html.Div(className="color-item"),
                    html.Div(className="color-item"),
                    html.Div(className="color-item"),
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
            html.Div([
                dcc.DatePickerSingle(date='2020-05-27',
                                     id="date-picker",
                                     display_format='MMM Do, YYYY'),
                dcc.Slider(id="hour-slider",
                           min=0,
                           max=23,
                           step=None,
                           marks={
                               0: "00:00",
                               1: '01:00',
                               2: '02:00',
                               3: '03:00',
                               4: '04:00',
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
                           },
                           value=5,
                           className="slider"),
            ], ),
            dcc.Graph(id='graph-with-slider-stations'),
            dcc.Graph(id='graph-with-slider-capacity'),
        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])


#------------------------------------------------------------------------------------------------
# FIGURE UPDATES
#------------------------------------------------------------------------------------------------


@app.callback(Output('graph-with-slider-stations', 'figure'),
              Input('date-picker', 'date'))
def update_figure_stations_lines(date):
    filtered_df_by_time = df_events[df_events['Date_time'].str.contains(date)]

    # y = filtered_df_by_time["Passengers_total"]
    x = [
        "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00",
        "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
        "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
    ]
    fig = go.Figure()
    for station in filtered_df_by_time["Station"]:
        station_by_time = (
            filtered_df_by_time[filtered_df_by_time["Station"] == station])
        fig.add_trace(
            go.Scatter(
                x=x,
                y=station_by_time["Passengers_total"],
                marker=dict(size=6),
                mode="lines+markers",
                name=station,
            ))
    title = "Crowdness through {date} for each station".format(date=date)
    fig.update_layout(title=title,
                      xaxis_title="Hour",
                      yaxis_title="Total Passengers")

    return fig


@app.callback(Output('graph-with-slider-capacity', 'figure'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_figure_stations_mobility(selected_hour, date):
    if selected_hour == 24:
        parsed_hour = "00"
    elif selected_hour > 9:
        parsed_hour = selected_hour
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)
    filtered_df_by_time = df_events[df_events["Date_time"] == filter]

    x = filtered_df_by_time["Station"]

    fig = go.Figure(
        go.Bar(x=x,
               y=filtered_df_by_time["Checked_in_passengers"],
               name='Check in'))

    fig.add_trace(
        go.Bar(x=x,
               y=filtered_df_by_time["Checked_out_passengers"],
               name='Check out'))
    fig.update_layout(barmode='stack')
    fig.update_xaxes(categoryorder='category ascending')

    fig.update_layout(transition_duration=500)
    title = "Check in and check out for {date} at {selected_hour}:00 o'clock".format(
        date=date, selected_hour=parsed_hour)
    fig.update_layout(title=title,
                      xaxis_title="Station",
                      yaxis_title="Check-in & Check-out")

    return fig


#------------------------------------------------------------------------------------------------
# IMAGE UPDATES
#------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------#


@app.callback(Output('Centraal', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Centraal(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Centraal Station")


@app.callback(Output('Centraal-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Centraal(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Centraal Station")


#-------------------------------------------------------------------------#
@app.callback(Output('Strandvliet', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Strandvliet(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Strandvliet")


@app.callback(Output('Strandvliet-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Strandvliet(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Strandvliet")


#-------------------------------------------------------------------------#


@app.callback(Output('Spaklerweg', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Spaklerweg(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events, "Spaklerweg")


@app.callback(Output('Spaklerweg-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Spaklerweg(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Spaklerweg")


#-------------------------------------------------------------------------#


@app.callback(Output('VanDerMadeweg', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_VanDerMadeweg(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Van der Madeweg")


@app.callback(Output('VanDerMadeweg-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_VanDerMadeweg(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Van der Madeweg")


#-------------------------------------------------------------------------#


@app.callback(Output('Zuid', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Zuid(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station Zuid")


@app.callback(Output('Zuid-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Zuid(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Station Zuid")


#-------------------------------------------------------------------------#


@app.callback(Output('Bijlmer', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Bijlmer(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station Bijlmer ArenA")


@app.callback(Output('Bijlmer-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Bijlmer(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Station Bijlmer ArenA")


#-------------------------------------------------------------------------#


@app.callback(Output('Duivendrecht', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Duivendrecht(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station Duivendrecht")


@app.callback(Output('Duivendrecht-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Duivendrecht(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Station Duivendrecht")


#-------------------------------------------------------------------------#


@app.callback(Output('NS', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_NS(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 52 North")


@app.callback(Output('NS-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_NS(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 52 North")


#-------------------------------------------------------------------------#


@app.callback(Output('RE', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RE(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 52 South")


@app.callback(Output('RE-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RE(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 52 South")


#-------------------------------------------------------------------------#


@app.callback(Output('NA', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_NA(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 51,53,54")


@app.callback(Output('NA-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_NA(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 51,53,54")


#-------------------------------------------------------------------------#


@app.callback(Output('VG', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_VG(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 52 South")


@app.callback(Output('VG-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_VG(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 52 South")


#-------------------------------------------------------------------------#


@app.callback(Output('BG', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_BG(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 50,54 South")


@app.callback(Output('BG-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_BG(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 50,54 South")


#-------------------------------------------------------------------------#


@app.callback(Output('IA', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_IA(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Joined Stations Line 50,51")


@app.callback(Output('IA-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_IA(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events,
                             "Joined Stations Line 50,51")


#-------------------------------------------------------------------------#


@app.callback(Output('RO', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RO(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station RAI")


@app.callback(Output('RO-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RO(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Station RAI")


#------------------------------------------------------------------------------------------------
# VENUES UPDATES
#------------------------------------------------------------------------------------------------


@app.callback(Output('arena', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    filter = create_filter_venues(selected_hour, date)
    filtered_df = df_venues[df_venues["Time_to_filter"] == filter]
    return filtered_df["At_ArenA_beginning_of_hour"]


@app.callback(Output('toekmost', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    filter = create_filter_venues(selected_hour, date)
    filtered_df = df_venues[df_venues["Time_to_filter"] == filter]
    return filtered_df["At_De_Toekmost_beginning_of_hour"]


@app.callback(Output('afas', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    filter = create_filter_venues(selected_hour, date)
    filtered_df = df_venues[df_venues["Time_to_filter"] == filter]
    return filtered_df["At_AFAS_beginning_of_hour"]


@app.callback(Output('ziggo', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_venue(selected_hour, date):
    filter = create_filter_venues(selected_hour, date)
    filtered_df = df_venues[df_venues["Time_to_filter"] == filter]
    return filtered_df["At_Ziggo_beginning_of_hour"]


#------------------------------------------------------------------------------------------------
# EVENT UPDATES
#------------------------------------------------------------------------------------------------

# @app.callback(Output('events', 'children'), Input('date-picker', 'date'))
# def return_recent_events(date):

# today_events = df_events[df_events["Date_time"].str.contains(date)
#                          & df_events["Event starting"] == 1]
# yesterday_events = df_events.loc[df_events["Date_time"].str.contains(
#     "2020-05-27").shift(-24 * 15) == 1]
# tomorrow_events = df_events.loc[df_events["Date_time"].str.contains(
#     "2020-05-27").shift(24 * 15) == 1]

# yesterday_events = yesterday_events[yesterday_events["Event starting"] ==
#                                     1]
# tomorrow_events = tomorrow_events[tomorrow_events["Event starting"] == 1]

# if(yesterday_events.empty):

# return (html.Div(className="event",
#                  children=[
#                      html.H2(
#                          date,
#                          className="venue-name",
#                      ),
#                      html.H2(
#                          "Today",
#                          className="venue-numbers",
#                      ),
#                  ]))

if __name__ == '__main__':

    app.run_server(debug=True, port=3000)