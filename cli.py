import argparse  
from core.pico_placa_predictor import PicoPlacaPredictor 
from core.pico_placa_regulations import PicoPlacaRegulations  
from core.pico_placa_rule import PicoPlacaRule  
from datetime import time  

def parse_arguments():
    """
    Parses command-line arguments for the license plate and date/time.

    :return: Parsed arguments as a namespace object.
    """
    parser = argparse.ArgumentParser(description="Plate validator")

    # Argument for the license plate
    parser.add_argument(
        '--plate',
        type=str,
        required=True,
        help='Licence plate of the vehicle in format XXX-####')

    # Argument for the date and time
    parser.add_argument(
        '--datehour',
        type=str,
        required=True,
        help='Date and time in format yyyy-mm-dd-hh:mm')

    return parser.parse_args()

def set_rules():
    """
    Defines the Pico y Placa rules for each weekday.

    :return: An instance of PicoPlacaRegulations containing all the rules.
    """
    # Define restriction time ranges
    restrictions_morning = (time(7, 0), time(9, 30))
    restrictions_noon = (time(16, 0), time(19, 30))

    regulations = PicoPlacaRegulations()

    # Add rules for each weekday
    regulations.addRule(PicoPlacaRule('Monday', [1, 2], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Tuesday', [3, 4], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Wednesday', [5, 6], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Thursday', [7, 8], [restrictions_morning, restrictions_noon]))
    regulations.addRule(PicoPlacaRule('Friday', [9, 0], [restrictions_morning, restrictions_noon]))

    return regulations

def main():
    """
    Main function to execute the Pico y Placa validation process.
    """
    # Parse command-line arguments
    args = parse_arguments()

    # Set up the regulations
    week_regulations = set_rules()
    pico_placa_predictor = PicoPlacaPredictor(week_regulations)

    # Validate the license plate and date/time
    is_restricted, reason = pico_placa_predictor.validation(args.plate, args.datehour)

    # Display the results
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


if __name__ == "__main__":
    main()

