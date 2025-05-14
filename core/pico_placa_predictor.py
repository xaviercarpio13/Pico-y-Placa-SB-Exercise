from utils.plate_parser import PlateParser
from utils.date_parser import DateParser

class PicoPlacaPredictor:

    @staticmethod
    def validation (licence_plate,date_time):
        if(PlateParser.validator_licence_plate(licence_plate)):
            print("primera validacion exitosa")
        if(DateParser.validator_date_time(date_time)):
            print("segunda validacion exitosa")
        
