import argparse
from core.pico_placa_predictor import PicoPlacaPredictor
from core.pico_placa_regulations import PicoPlacaRegulations
from core.pico_placa_rule import PicoPlacaRule
from datetime import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Plate validator")

    parser.add_argument(
        '--plate',
        type=str,
        required=True,
        help='Licence plate of the vehicule in format XXX-####')
    
    parser.add_argument(
        '--datehour',
        type=str,
        required=True,
        help='Date and time in format yyyy-mm-dd-hh:mm')

    return parser.parse_args()

def set_rules():
    restrictions_morning = (time(7, 0), time(9, 30))
    restrictions_noon = (time(16, 0), time(19, 30))

    regulations=PicoPlacaRegulations()

    regulations.addRule(PicoPlacaRule('Monday', [1, 2], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Tuesday', [3, 4], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Wednesday', [5, 6], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Thursday', [7, 8], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Friday', [9, 0], [restrictions_morning, restrictions_noon]))
    

    return regulations

def main():
    
    args=parse_arguments()
    
    week_regulations=set_rules()
    pico_placa_predictor = PicoPlacaPredictor(week_regulations)
    is_restricted,reason=pico_placa_predictor.validation(args.plate,args.datehour)
    
    print("\n========== PICO Y PLACA CHECK RESULT ==========\n")
    print(f"License Plate: {args.plate}")
    print(f"Date & Time : {args.datehour}\n")

    if is_restricted:
        print("STATUS:       VEHICLE IS RESTRICTED")
        print("RESTRICTED HOURS: 7:00 - 9:30 | 16:00 - 19:30")
    else:
        print("STATUS      : VEHICLE IS NOT RESTRICTED")

    print(f"REASON      : {reason}")
    print("\n===============================================\n")

if __name__=="__main__":
    main()

