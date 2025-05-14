import argparse
from core.pico_placa_predictor import PicoPlacaPredictor

def parse_arguments():
    parser = argparse.ArgumentParser(description="Plate validator")

    parser.add_argument(
        '--plate',
        type=str,
        required=True,
        help='Licence plate of the vehicule in format XXX-####')

    return parser.parse_args()

def main():
    
    args=parse_arguments()
    predictor=PicoPlacaPredictor()
    predictor.validation(args.plate)




if __name__=="__main__":
    main()

