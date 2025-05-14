from utils.plate_parser import PlateParser

class PicoPlacaPredictor:

    @staticmethod
    def validation (licence_plate):
        if(PlateParser.validator_licence_plate(licence_plate)):
            print("primera validacion exitosa")
