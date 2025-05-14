import argparse
from core.pico_placa_predictor import PicoPlacaPredictor
from utils.date_parser import DateParser

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

def main():
    
    args=parse_arguments()
    predictor=PicoPlacaPredictor()
    predictor.validation(args.plate,args.datehour)




if __name__=="__main__":
    main()

