from core.pico_placa_rule import PicoPlacaRule

class PicoPlacaRegulations:
    """
    This class manages a collection of PicoPlacaRule objects and provides methods 
    to add rules and check restrictions based on license plate digits, day, and time.
    """
    def __init__(self):
        self.rules = []

    def addRule(self, rule: PicoPlacaRule):
        """
        Adds a PicoPlacaRule object to the list of rules.

        :param rule: An instance of PicoPlacaRule to be added.
        """
        self.rules.append(rule)

    def checkRestrictions(self, last_digit_plate, day_time):
        """
        Checks if a vehicle is restricted based on the last digit of its plate, 
        the day of the week, and the time.

        :param last_digit_plate: The last digit of the vehicle's license plate.
        :param day_time: A tuple containing the day of the week (e.g., "Monday") 
                         and the time (e.g., "08:30").
        :return: The result of the restriction check from the corresponding rule.
        :raises ValueError: If no rules are defined for the given day.
        """
        day_name, time_input = day_time  # Unpack the day and time from the input tuple

        # Find the rule that matches the given day
        rule = next((rule for rule in self.rules if rule.weekday == day_name), None)

        if rule:
            # If a matching rule is found, verify the restriction
            return rule.verify_pico_placa(last_digit_plate, day_name, time_input)
        else:
            # Raise an error if no rules are defined for the given day
            raise ValueError(f"No hay reglas definidas para el día: {day_name}")

