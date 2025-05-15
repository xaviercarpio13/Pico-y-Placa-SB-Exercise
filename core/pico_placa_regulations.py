from core.pico_placa_rule import PicoPlacaRule
from datetime import time

class PicoPlacaRegulations:
    def __init__(self):
        self.rules=[]

    def addRule(self, rule:PicoPlacaRule):
        self.rules.append(rule)
    
    def checkRestrictions(self, last_digit_plate, day_time):
        day_name, time_input = day_time
        print(last_digit_plate,day_name, time_input)
        rule = next((r for r in self.rules if r.weekday==day_name), None)
        if rule:
            return rule.verify_pico_placa(last_digit_plate, day_name,time_input)
        else:
            raise ValueError(f"No hay reglas definidas para el día: {day_name}")
        
    