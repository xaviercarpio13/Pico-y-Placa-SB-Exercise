class PicoPlacaRule:
    def __init__(self, day, plates_restricted, time_ranges):
        """
        Initializes the PicoPlacaRule object with the day of the week, restricted plate digits, 
        and time ranges during which the restriction applies.

        :param day: The day of the week when the rule applies (e.g., "Monday").
        :param plates_restricted: A list of integers representing the last digits of plates restricted on this day.
        :param time_ranges: A list of tuples representing time ranges (start_time, end_time) for the restriction.
        """
        self.weekday = day
        self.digits_restricted = plates_restricted
        self.time_ranges = time_ranges

    def is_time_in_ranges(self, input_time):
        """
        Checks if the given time falls within any of the restricted time ranges.

        :param input_time: The time to check (e.g., "08:30").
        :return: True if the time is within any restricted range, False otherwise.
        """
        for start_time, end_time in self.time_ranges:
            if start_time <= input_time <= end_time:
                return True
        return False

    def verify_pico_placa(self, last_digit, day_input, time_input):
        """
        Verifies if a vehicle is restricted based on the last digit of its plate, the day, and the time.

        :param last_digit: The last digit of the vehicle's license plate.
        :param day_input: The current day of the week.
        :param time_input: The current time.
        :return: A tuple (is_restricted, message) where:
                 - is_restricted is True if the vehicle is restricted, False otherwise.
                 - message provides details about the restriction status.
        """

        
        # Check if the rule applies to the given day
        if day_input != self.weekday:
            return False, f"No restriction today ({day_input}). Rule applies only on {self.weekday}."

        # Check if the last digit of the plate is restricted
        if int(last_digit) not in self.digits_restricted:
            return False, f"Vehicle with plate ending in {last_digit} is not restricted on {self.weekday}."

        # Check if the current time falls within the restricted time ranges
        if not self.is_time_in_ranges(time_input):
            return False, "Vehicle is restricted today, but current time is outside the restriction hours."

        # If all conditions are met, the vehicle is restricted
        return True, f"On {day_input}, plates ending in {last_digit} are restricted at this time {time_input}."


