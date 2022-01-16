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
    if selected_hour == 24:
        parsed_hour = "00"
    elif selected_hour > 9:
        parsed_hour = selected_hour
    else:
        parsed_hour = "0" + str(selected_hour)
    filter = "{date} {selected_hour}:00:00".format(date=date,
                                                   selected_hour=parsed_hour)
    filtered_df_by_time = df[df["Date_time"] == filter]
    filtered_df_by_station = filtered_df_by_time[filtered_df_by_time["Station"]
                                                 == station_name]
    total = filtered_df_by_station["Passengers_total"]
    if (total > (500 + (500 * 0.6))).bool():
        return {'background-color': 'green'}
    elif (total > 500 + 500 * 0.3).bool():
        return {'background-color': 'orange'}
    elif (total > 500).bool():
        return {'background-color': 'red'}