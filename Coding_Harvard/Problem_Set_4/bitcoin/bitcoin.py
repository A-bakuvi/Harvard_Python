import requests
import sys
import json


def main():

    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        number_ofBitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit(1)
    try:
        return_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        turning_toJson = return_json.json()
        price = turning_toJson["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit(1)
    bitcon_price = number_ofBitcoins * price
    print(f"${bitcon_price:,.4f}")



if __name__ == "__main__":
    main()