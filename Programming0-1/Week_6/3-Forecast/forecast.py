def forecast(days):
    sunshine_count = days.count('sunshine')
    rain_count = days.count('rain')
    snow_count = days.count('snow')
    score = [sunshine_count, rain_count, snow_count]
    max_count = max(score)
    if score.count(max_count) == 3:
        return days[-1:][0]
    elif score.count(max_count) == 2:
        index = score.index(min(score))
        if index == 0:
            return 'sunshine'
        elif index == 1:
            return 'rain'
        else:
            return 'snow'
    elif max_count == sunshine_count:
        return 'sunshine'
    elif max_count == rain_count:
        return 'rain'
    else:
        return 'snow'

# print(forecast(["snow", "snow", "rain", "sunshine"]))
# print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
# print(forecast(["rain", "rain", "sunshine", "sunshine"]))
