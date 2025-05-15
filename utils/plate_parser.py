import re 

class PlateParser:
    """
    A utility class for validating and parsing license plate strings.
    """

    @staticmethod
    def validator_licence_plate(licence_plate_str):
        """
        Validates the format of a license plate string and extracts the last digit.

        :param licence_plate_str: A string representing the license plate in the format 'XXX-####'.
        :return: The last digit of the license plate as a string.
        :raises ValueError: If the license plate does not match the expected format.
        """
        # Validate the license plate format using a regular expression
        if not re.fullmatch('^[A-X]{3}-[0-9]{4}', licence_plate_str):
            raise ValueError(
                "Invalid format of licence plate. Expected XXX-####"
            )
        
        # Return the last character (digit) of the license plate
        list_digits = list(licence_plate_str)
        return list_digits[-1]





