from lib2to3.pgen2.token import STRING
from dash import html
import datetime

from markupsafe import string


def create_filter_venues(selected_hour, date):
    if selected_hour == 24:
        parsed_hour = "00"
    elif selected_hour > 9:
        parsed_hour = selected_hour
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)
    return filter


def create_filter_stations(selected_hour, date, df, station_name):
    filter = create_filter_venues(selected_hour, date)
    filtered_df_by_time = df[df["Date_time"] == filter]
    filtered_df_by_station = filtered_df_by_time[filtered_df_by_time["Station"]
                                                 == station_name]
    baseline = filtered_df_by_station["Passengers_total_BASELINE"]
    total = filtered_df_by_station["Passengers_total"]
    if (total > (baseline + (baseline * 0.6))).bool():
        return {'background-color': 'red'}
    elif (total > baseline + baseline * 0.3).bool():
        return {'background-color': 'orange'}
    elif (total > baseline).bool():
        return {'background-color': 'green'}


def create_hover_info(selected_hour, date, df, station_name, predictions):

    filter = create_filter_venues(selected_hour, date)

    if ("2021" in date) & ("11" in date) & (("15" in date) or ("16" in date) or
                                            ("16" in date) or ("17" in date) or
                                            ("19" in date) or ("18" in date) or
                                            ("20" in date) or ("21" in date)):
        filtered_predictions_by_time = predictions[predictions["ds"] == filter]
        filtered_predictions_by_station = filtered_predictions_by_time[
            filtered_predictions_by_time["Station"] == station_name]
        estimate_ci = filtered_predictions_by_station[
            "check_in_prediction"].values
        estimate_co = filtered_predictions_by_station[
            "check_out_prediction"].values
        estimate_text = "Estimate :{estimate}(ci: {estimate_ci} + co: {estimate_co})".format(
            estimate=round(estimate_ci[0]) + round(estimate_co[0]),
            estimate_ci=round(estimate_ci[0]),
            estimate_co=round(estimate_co[0]))

        filtered_df_by_time = df[df["Date_time"] == filter]
        filtered_df_by_station = filtered_df_by_time[
            filtered_df_by_time["Station"] == station_name]
        baseline = filtered_df_by_station["Passengers_total_BASELINE"].values
        total = filtered_df_by_station["Passengers_total"].values

        baseline_text = "Baseline :{baseline}".format(
            baseline=round(baseline[0]))
        total_text = "At this hour :{total}".format(total=round(total[0]))
        return (html.Div(className="info-hover".format(
            station_name=station_name.replace(" ", "-"))),
                html.Div(children=[
                    html.Div(className="hover-container",
                             children=[
                                 html.H2(total_text,
                                         className="info-hover-text"),
                                 html.H2(baseline_text,
                                         className="info-hover-text"),
                                 html.H2(estimate_text,
                                         className="info-hover-text"),
                             ])
                ],
                         className="hide"))
    else:
        filtered_df_by_time = df[df["Date_time"] == filter]
        filtered_df_by_station = filtered_df_by_time[
            filtered_df_by_time["Station"] == station_name]
        baseline = filtered_df_by_station["Passengers_total_BASELINE"].values
        total = filtered_df_by_station["Passengers_total"].values

        baseline_text = "Baseline :{baseline}".format(
            baseline=round(baseline[0]))
        total_text = "At this hour :{total}".format(total=round(total[0]))
        return (html.Div(className="info-hover".format(
            station_name=station_name.replace(" ", "-"))),
                html.Div(children=[
                    html.Div(className="hover-container",
                             children=[
                                 html.H2(total_text,
                                         className="info-hover-text"),
                                 html.H2(baseline_text,
                                         className="info-hover-text"),
                             ])
                ],
                         className="hide"))
