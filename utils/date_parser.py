import datetime
class DateParser:

    @staticmethod
    def validator_date_time(date_time):
        ## yyyy-mm-dd-hh:mm
        format='%Y-%m-%d-%H:%M'
        try:
            res = datetime.datetime.strptime(date_time, format)
            day_of_week = res.strftime('%A')  # Day of the week
            hour=res.time()
            return[day_of_week,hour]
        except ValueError:
            raise ValueError("Invalid date and time format. Expected: yyyy-mm-dd-hh:mm")
    

