import re
class PlateParser ():
    @staticmethod
    def validator_licence_plate (licence_plate_str):
        try:
            re.fullmatch('^[A-X]{3}-[0-9]{4}',licence_plate_str)
            list_digits=list(licence_plate_str)
            return list_digits[-1]
        except ValueError:
            raise ValueError(
                "Invalid format of licence plate. Expected XXX-####"
            )
        



    