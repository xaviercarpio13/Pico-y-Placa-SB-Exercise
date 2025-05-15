import datetime 

class DateParser:
    """
    A utility class for parsing and validating date and time inputs.
    """

    @staticmethod
    def validator_date_time(date_time):
        """
        Validates and parses a date-time string into a day of the week and time.

        :param date_time: A string representing the date and time in the format 'yyyy-mm-dd-hh:mm'.
        :return: A list containing the day of the week (e.g., "Monday") and the time object.
        :raises ValueError: If the input string does not match the expected format.
        """
        # Define the expected date-time format
        format = '%Y-%m-%d-%H:%M'
        try:
            # Parse the input string into a datetime object
            result = datetime.datetime.strptime(date_time, format)
            day_of_week = result.strftime('%A')
            hour = result.time()

            # Return the day of the week and time as a list
            return [day_of_week, hour]
        except ValueError:
            # Raise an error if the input string does not match the expected format
            raise ValueError("Invalid date and time format. Expected: yyyy-mm-dd-hh:mm")
