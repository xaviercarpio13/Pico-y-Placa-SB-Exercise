from utils.plate_parser import PlateParser 
from utils.date_parser import DateParser  
from core.pico_placa_regulations import PicoPlacaRegulations  


class PicoPlacaPredictor:
    """
    This class predicts whether a vehicle is restricted based on its license plate, 
    the date, and the time, using the PicoPlacaRegulations.
    """
    def __init__(self, regulations: PicoPlacaRegulations):
        """
        Initializes the PicoPlacaPredictor with a set of regulations.

        :param regulations: An instance of PicoPlacaRegulations containing the rules.
        """
        self.regulations = regulations

    def validation(self, licence_plate, date_time):
        """
        Validates whether a vehicle is restricted based on its license plate and the date/time.

        :param licence_plate: The license plate of the vehicle.
        :param date_time: The date and time to check (e.g., "Monday 08:30").
        :return: The result of the restriction check from the regulations.
        """
        # Validate and extract the last digit of the license plate
        last_digit_plate = PlateParser.validator_licence_plate(licence_plate)

        # Validate and parse the date and time
        day_time = DateParser.validator_date_time(date_time)

        # Check the restrictions using the regulations
        result = self.regulations.checkRestrictions(last_digit_plate, day_time)
        return result

