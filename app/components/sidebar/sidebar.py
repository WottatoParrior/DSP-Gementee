from dash import dcc, html
import dash_bootstrap_components as dbc

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


def generate_sidenav():
    return html.Div(
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
    )


def generate_content():
    return html.Div(id="page-content", children=[], style=CONTENT_STYLE)


def generate_sidebar():
    return html.Div(
        [dcc.Location(id="url"),
         generate_sidenav(),
         generate_content()])
