from dash import dcc, html

SLIDER_STYLE = {"padding-top : 20px"}


def generate_datepicker():
    return dcc.DatePickerSingle(date='2021-01-21', display_format='MMM Do, YY')


def generate_day_slider():
    return dcc.Slider(min=5,
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
                      className="slider")


def generate_date_hour_picker():
    return html.Div([
        generate_datepicker(),
        generate_day_slider(),
    ], )
