class PicoPlacaRule:
    def __init__(self, day, plates_restricted, time_ranges):
        self.weekday = day
        self.digits_restricted = plates_restricted
        self.time_ranges=time_ranges

    def is_time_in_ranges(self, input_time):
        for start_time, end_time in self.time_ranges:
            if start_time <= input_time <= end_time:
                return True
        return False
        
    
    def verify_pico_placa(self, last_digit, day_input, time_input):
        if day_input != self.weekday:
            return False, f"No restriction today ({day_input}). Rule applies only on {self.weekday}."
        if int(last_digit) not in self.digits_restricted:
            return False, f"Vehicle with plate ending in {last_digit} is not restricted on {self.weekday}."
        if not self.is_time_in_ranges(time_input):
            return False, "Vehicle is restricted today, but current time is outside the restriction hours."
        return True, f"On {day_input}, plates ending in {last_digit} are restricted at this time {time_input}."
    
    
