class PicoPlacaRule:
    def __init__(self, day, plates_restricted, time_ranges):
        self.weekday = day
        self.digits_restricted = plates_restricted
        self.time_ranges=time_ranges
        #time_ranges=[(06:00:00,09:00:00),(16:00:00,20:00:00)]


    def is_time_in_ranges(self, input_time):
        for start_time, end_time in self.time_ranges:
            if start_time <= input_time <= end_time:
                return True
        return False
        
    
    def verify_pico_placa(self, last_digit, day_input, time_input):
        if day_input != self.weekday:
            return False
        if last_digit not in self.digits_restricted:
            return False
        return self.is_time_in_ranges(time_input)
    
    
