from utils.plate_parser import PlateParser
from utils.date_parser import DateParser


class PicoPlacaPredictor:

    @staticmethod
    def validation (licence_plate,date_time):
        plate=PlateParser.validator_licence_plate(licence_plate)
        day_time=DateParser.validator_date_time(date_time)
        print(plate,day_time)
