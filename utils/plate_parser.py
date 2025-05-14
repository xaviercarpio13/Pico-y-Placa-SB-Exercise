import re
class PlateParser ():
    @staticmethod
    def validator_licence_plate (licence_plate_str):
        if re.fullmatch('^[A-X]{3}-[0-9]{4}',licence_plate_str):
            return True
        else:
            raise ValueError(
                "Invalid format of licence plate. Expected XXX-####"
            )
        



    