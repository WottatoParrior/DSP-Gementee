import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date
from helpers.helpers import create_filter_venues, create_filter_stations, create_hover_info
import plotly.graph_objects as go
import dash_table

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

df_venues = pd.read_csv("../data/venues.csv")
df_events = pd.read_csv("../data/events.csv")
df_events_schedule = pd.read_csv("../data/events_to_display.csv")
df_predictions = pd.read_csv("../data/predictions.csv")

image_filename = "assets/metro.jpg"

app = dash.Dash(__name__,
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                ],
                suppress_callback_exceptions=True)
app.title = 'Mobility Management'

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
                dcc.DatePickerSingle(date='2021-10-23',
                                     id="date-picker",
                                     min_date_allowed=date(2020, 1, 1),
                                     max_date_allowed=date(2021, 11, 21),
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
                    html.Div("Color Codes",
                             style={
                                 "width": "100%",
                                 "font-weight": "900"
                             }),
                    html.Div("None", className="color-item no-color"),
                    html.Div("- Less than regular crowdness",
                             className="color-item"),
                    html.Div(className="color-item green"),
                    html.Div("- 0%-30% Increased crowdness",
                             className="color-item"),
                    html.Div(className="color-item orange"),
                    html.Div("- 31%-60% Increased crowdness",
                             className="color-item"),
                    html.Div(className="color-item red"),
                    html.Div("- 60%+ Increased crowdness",
                             className="color-item"),
                ])
        ]
    elif pathname == "/venues":
        return [
            html.H1('Insights about venues', style={'textAlign': 'center'}),
            html.Div([
                dcc.DatePickerSingle(date='2021-10-23',
                                     id="date-picker",
                                     min_date_allowed=date(2020, 1, 1),
                                     max_date_allowed=date(2021, 11, 21),
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
            dcc.Graph(id='venues-graph', style={'display': 'inline-block'}),
            dcc.Graph(id='venues-graph2', style={'display': 'inline-block'}),
            html.Div([
                html.H4(children='List of events'),
                #dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
                dash_table.DataTable(
                    id='table-filter',
                    data=df_events_schedule.to_dict('records'),
                    columns=[
                        {
                            'id': 'ID',
                            'name': 'ID'
                        },
                        {
                            'id': 'Date',
                            'name': 'Date'
                        },
                        {
                            'id': 'Titel',
                            'name': 'Titel'
                        },
                        {
                            'id': 'Starting time',
                            'name': 'Starting time'
                        },
                        {
                            'id': 'Opening time',
                            'name': 'Opening time'
                        },
                        {
                            'id': 'Ending time',
                            'name': 'Ending time'
                        },
                        {
                            'id': 'Location',
                            'name': 'Location'
                        },
                        {
                            'id': 'Expected visitors',
                            'name': 'Expected visitors'
                        },
                        {
                            'id': 'Capacity of location',
                            'name': 'Capacity of location'
                        },
                        {
                            'id': '%',
                            'name': 'Expected location saturation'
                        },
                    ],
                    style_as_list_view=True,
                    style_cell={'padding': '5px'},
                    style_header={
                        'backgroundColor': 'white',
                        'fontWeight': 'bold',
                        'font-family': 'sans-serif'
                    },
                    style_data={'font-family': 'sans-serif'})
            ])
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
            html.Div([
                html.H4(children=''),
                dbc.Table.from_dataframe(df_events_schedule,
                                         striped=True,
                                         bordered=True,
                                         hover=True)
            ])
        ]
    elif pathname == "/stations":
        return [
            html.Div([
                dcc.DatePickerSingle(date='2021-10-23',
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
                      yaxis_title="Total Passengers",
                      showlegend=False)

    return fig


@app.callback(Output('graph-with-slider-capacity', 'figure'),
              Input('date-picker', 'date'), Input('hour-slider', 'value'))
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

    fig1 = go.Figure(
        go.Bar(x=x,
               y=filtered_df_by_time["Checked_in_passengers"],
               name='Check in'))

    fig1.add_trace(
        go.Bar(x=x,
               y=filtered_df_by_time["Checked_out_passengers"],
               name='Check out'))
    fig1.update_xaxes(categoryorder='category ascending')

    title = "Check in and check out".format(filter=filter)
    fig1.update_layout(title=title,
                       xaxis_title="Station",
                       yaxis_title="Check-in & Check-out",
                       barmode='stack')

    return fig1


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
                             "Centraal Station", df_predictions)


#-------------------------------------------------------------------------#
@app.callback(Output('Strandvliet', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Strandvliet(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Strandvliet")


@app.callback(Output('Strandvliet-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Strandvliet(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Strandvliet",
                             df_predictions)


#-------------------------------------------------------------------------#


@app.callback(Output('Spaklerweg', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Spaklerweg(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events, "Spaklerweg")


@app.callback(Output('Spaklerweg-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_Spaklerweg(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Spaklerweg",
                             df_predictions)


#-------------------------------------------------------------------------#


@app.callback(Output('VanDerMadeweg', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_VanDerMadeweg(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Van der Madeweg")


@app.callback(Output('VanDerMadeweg-info', 'children'),
              Input('hour-slider', 'value'), Input('date-picker', 'date'))
def update_style_VanDerMadeweg(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Van der Madeweg",
                             df_predictions)


#-------------------------------------------------------------------------#


@app.callback(Output('Zuid', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Zuid(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station Zuid")


@app.callback(Output('Zuid-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_Zuid(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Station Zuid",
                             df_predictions)


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
                             "Station Bijlmer ArenA", df_predictions)


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
                             "Station Duivendrecht", df_predictions)


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
                             "Joined Stations Line 52 North", df_predictions)


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
                             "Joined Stations Line 52 South", df_predictions)


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
                             "Joined Stations Line 51,53,54", df_predictions)


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
                             "Joined Stations Line 52 South", df_predictions)


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
                             "Joined Stations Line 50,54 South",
                             df_predictions)


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
                             "Joined Stations Line 50,51", df_predictions)


#-------------------------------------------------------------------------#


@app.callback(Output('RO', 'style'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RO(selected_hour, date):
    return create_filter_stations(selected_hour, date, df_events,
                                  "Station RAI")


@app.callback(Output('RO-info', 'children'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_style_RO(selected_hour, date):
    return create_hover_info(selected_hour, date, df_events, "Station RAI",
                             df_predictions)


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


@app.callback(Output('events', 'children'), Input('date-picker', 'date'))
def return_recent_events(date):
    today_events = df_events_schedule[df_events_schedule["Date"].str.contains(
        date)]
    event_names = today_events["Titel"].values
    event_time = today_events["Starting time"].values
    event_location = today_events["Location"].values
    event_visitors = today_events["Expected visitors"].values
    arr = []
    count = 0
    for event_name in event_names:
        arr.append(
            html.Div(className="event",
                     children=[
                         html.H2(
                             event_name,
                             className="event-name",
                         ),
                         html.H2(
                             event_location,
                             className="event-location",
                         ),
                         html.H2(
                             event_time[count],
                             className="event-time",
                         ),
                         html.H2(
                             "Expected Visitors : {event_visitors}".format(
                                 event_visitors=event_visitors[count]),
                             className="event-numbers",
                         )
                     ]))
        count = count + 1

    return arr


#------------------------------------------------------------------------------------------------
# VENUES TAB
#------------------------------------------------------------------------------------------------


@app.callback(Output('venues-graph', 'figure'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_figure_stations_mobility(selected_hour, date):
    if selected_hour == 24:
        parsed_hour = "00"
    elif selected_hour > 9:
        parsed_hour = selected_hour
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)
    filtered_df_by_time = df_venues[df_venues["Time_to_filter"] == filter]

    at_arena = int(filtered_df_by_time["At_ArenA_end_of_hour"])
    at_afas = int(filtered_df_by_time["At_AFAS_end_of_hour"])
    at_zigo = int(filtered_df_by_time["At_Ziggo_end_of_hour"])
    at_detoekomst = int(filtered_df_by_time["At_De_Toekmost_end_of_hour"])

    venues = ['ArenA', 'AFAS', 'Ziggo', 'DeToekmost']

    fig = go.Figure(
        [go.Bar(x=venues, y=[at_arena, at_afas, at_zigo, at_detoekomst])])

    title = "Visitors at venues on {date} at {selected_hour}:00 o'clock".format(
        date=date, selected_hour=parsed_hour)

    fig.update_layout(title=title,
                      yaxis_range=[0, 55000],
                      xaxis_title="Venues",
                      yaxis_title="Visitors",
                      width=600,
                      height=400)

    fig.add_layout_image(
        dict(
            source=
            "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/naphthalene.png",
            x=0.9,
            y=0.3,
        ))

    return fig


@app.callback(Output('venues-graph2', 'figure'), Input('hour-slider', 'value'),
              Input('date-picker', 'date'))
def update_figure_stations_mobility2(selected_hour, date):
    if selected_hour == 24:
        parsed_hour = "00"
    elif selected_hour > 9:
        parsed_hour = selected_hour
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)
    filtered_df_by_time = df_events[(df_events["Date_time"] == filter) & (
        df_events["Station"] == "Station Bijlmer ArenA")]

    check_in = int(filtered_df_by_time["Checked_in_passengers"])
    #check_in_baseline = int(filtered_df_by_time["Checked_in_passengers_BASELINE"])
    check_out = int(filtered_df_by_time["Checked_out_passengers"])
    #check_out_baseline = int(filtered_df_by_time["Checked_out_passengers_BASELINE"])

    labels = ['Checked in', 'Checked out']

    fig = go.Figure([go.Bar(x=labels, y=[check_in, check_out])])

    title = "Passengers at Bijlmer ArenA station"
    fig.update_layout(title=title,
                      yaxis_range=[0, 2500],
                      xaxis_title="Travel way",
                      yaxis_title="Passengers",
                      width=400,
                      height=400,
                      bargap=0.3)

    return fig


#------------------------------------------------------------------------------------------------
# EVENTS TAB
#------------------------------------------------------------------------------------------------


@app.callback(Output('table-filter', 'data'), Input('date-picker', 'date'))
def update_table(date):
    return df_events_schedule[df_events_schedule["Date"] == date].to_dict(
        'records')


if __name__ == '__main__':

    app.run_server(port=3000)