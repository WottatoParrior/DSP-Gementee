#Arima try
library(fpp3)
library(tidyverse)

#load pre-processed data
data <- read_csv('/home/timothy/Downloads/DSP/M_GVB_weather_events_all_covidindex_holidays_filled (1).csv' )
#new data: '/home/timothy/Downloads/DSP/Mobility preprocessing/M_GVB_weather_events_all_covidindex_holidays_filled.csv'
#remove douplicates
douplicates_data <- duplicates(data, key = Station, index = Date_time) #inspect douplicates
data_no_duplicates <- data[!duplicated(data[c('Station', 'Date_time')]), ]#get rid of dublicates
#turn into tsibble
data_tsibble <- data_no_duplicates %>%  as_tsibble(index = Date_time, key = Station)


###Fill missing data gaps
#looking into the gaps
any(tsibble::has_gaps(data_tsibble)[[".gaps"]]) #yes there are gaps
missing_data <- tsibble::scan_gaps(data_tsibble) 
#make missing values explicit
data_filled_ts <- data_tsibble %>% fill_gaps()
#check if worked
any(tsibble::has_gaps(data_filled_ts)[[".gaps"]])#no more gaps, so it worked


###Plot for eda for centraal sstation
#plot visiters per time period at centrall station
data_filled_ts %>% filter(Station == 'Centraal Station') %>% autoplot(Passengers_total)

#plot seasonality
data_filled_ts %>% filter(Station == 'Centraal Station') %>% gg_season(Passengers_total)


# First modeling tries ----------------------------------------------------
data_filled_ts = data_filled_ts %>% mutate(weekend = weekday_5.0 + weekday_6.0)

#create train and test set
train <- data_filled_ts %>% filter(Date_time < '2021-11-1')
test <- data_filled_ts %>% filter(Date_time >= '2021-11-1') #too long now, cut
validation <- train %>% filter(Date_time >= '2021-10-1') #check that its just 28 days and not 30
train <- train %>% filter(Date_time < '2021-10-1')


nrow(train) + nrow(test) + nrow(validation) == nrow(data_filled_ts) #checking if I split it correctly


#first model without anything
model <- train %>% model(ARIMA(Passengers_total))
fc <- model %>% forecast(validation)
accuracy(fc, validation)

#model with important dummy variables
model_comparrisions <- train %>% model(baseline = ARIMA(Passengers_total), 
                                       dow      = ARIMA(Passengers_total ~ weekday_1.0 + weekday_2.0 + weekday_3.0 + weekday_4.0 + weekday_5.0 + weekday_6.0), 
                                       weekend  = ARIMA(Passengers_total ~ weekend), 
                                       weatherh = ARIMA(Passengers_total ~ `Temp(F)` + `Wind(MpH)` + sum_rain_knmi + duration_rain_knmi), 
                                       knmi     = ARIMA(Passengers_total ~ duration_rain_knmi + avg_wind_speed_knmi + avg_temp_knmi + sum_rain_knmi), 
                                       holiday1 = ARIMA(Passengers_total ~ Is_Holiday_Binary), 
                                       holiday2 = ARIMA(Passengers_total ~ `Holiday_Boxing Day, Christmas holiday` +  `Holiday_Christmas Day, Christmas holiday` + `Holiday_Easter Monday` + `Holiday_Good Friday` + 
                                                                            `Holiday_Summer holiday` + `Holiday_Carnival holiday` + `Holiday_Christmas holiday` + `Holiday_Easter Sunday` + `Holiday_King's day` +
                                                                            `Holiday_Liberation Day, May holiday` + `Holiday_Whit Monday` + `Holiday_Ascension Thursday` + `Holiday_Carnival, Carnival holiday` +
                                                                            `Holiday_Christmas holiday, New year` + `Holiday_Fall holiday` + `Holiday_King's day, May holiday` + `Holiday_May holiday` + `Holiday_Whit Sunday`), 
                                       events = ARIMA(Passengers_total ~ StringencyIndex + `Event starting` + BezoekersVerwacht + `Event ending` + `C3_Cancel public events_1.0` + `C3_Cancel public events_2.0`))
                                       
                           


fc_comparrison <- model_comparrisions %>% forecast(validation)

accuracy_comparrison <- accuracy(fc_comparrison, validation)

accuracy_comparrison %>% group_by(.model) %>% summarize(RMSE = mean(RMSE, na.rm = T), MAE=mean(MAE, na.rm = T))



#Fourier terms and one events model
models_f <- train %>% model(k1 = ARIMA(Passengers_total ~ fourier(K = 1)), 
                            k2 = ARIMA(Passengers_total ~ fourier(K = 2)),
                            k3 = ARIMA(Passengers_total ~ fourier(K = 3)),
                            k4 = ARIMA(Passengers_total ~ fourier(K = 4)),
                            k5 = ARIMA(Passengers_total ~ fourier(K = 5)),
                            k6 = ARIMA(Passengers_total ~ fourier(K = 6)),
                            baseline = ARIMA(Passengers_total), 
                            events = ARIMA(Passengers_total ~ StringencyIndex + `Event starting` + 
                                           BezoekersVerwacht + `Event ending` + `C3_Cancel public events_1.0` + 
                                           `C3_Cancel public events_2.0` + weekend + Is_Holiday_Binary + `Temp(F)` + 
                                            `Wind(MpH)` + sum_rain_knmi + duration_rain_knmi))



fc_f <- models_f %>% forecast(validation)
accuracy_f <- accuracy(fc_f, validation)

accuracy_f %>% group_by(.model) %>% summarize(RMSE = mean(RMSE, na.rm = T), MAE=mean(MAE, na.rm = T))



event_model <- train %>% model(base = ARIMA(Passengers_total),
                                  event = ARIMA(Passengers_total ~ weekend + `Event starting` + `Event ending` + BezoekersVerwacht + 
                                                  StringencyIndex + `C3_Cancel public events_1.0` + `C3_Cancel public events_2.0`))



event_fc %>% event_model %>% forecast(validation)










