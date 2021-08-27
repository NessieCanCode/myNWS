import sys
import requests

county_code = sys.argv[1]


def get_parse(arg):
    url = "https://api.weather.gov/alerts/active?zone="+arg

    response = requests.get(url)
    data = response.json()
    nws_alert_headline = data['features'][0]['properties']['headline']
    nws_alert_description = data['features'][0]['properties']['description']
    return nws_alert_headline, nws_alert_description


if __name__ == '__main__':
    print(get_parse(county_code))
