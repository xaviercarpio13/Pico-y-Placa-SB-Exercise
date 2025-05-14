from utils.plate_parser import PlateParser
from utils.date_parser import DateParser
from core.pico_placa_regulations import PicoPlacaRegulations


class PicoPlacaPredictor:

    @staticmethod
    def validation (licence_plate,date_time):
        last_digit_plate=PlateParser.validator_licence_plate(licence_plate)
        day_time=DateParser.validator_date_time(date_time)
        regulations=PicoPlacaRegulations()
        if regulations.checkRestrictions(last_digit_plate,day_time):
            print ("Tiene pico y placa")
        else:
            print ("NO tiene pico y placa")

