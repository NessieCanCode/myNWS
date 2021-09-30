import json
import requests


def lambda_handler(event, context):
    county_code = event['queryStringParameters']['county_code']
    if str(county_code) != "demo":
        url = "https://api.weather.gov/alerts/active/zone/" + county_code
    else:
        url = "https://api.weather.gov/alerts?active=true&status=actual&message_type=alert"

    response = requests.get(url)
    data = response.json()
    if data['features'][0]['properties']['headline'] == None:
            try:
                for i in range(0, 11):
                    if data['features'][i]['properties']['headline'] != none:
                        nws_alert_headline = data['features'][i]['properties']['headline']
                        nws_alert_description = data['features'][i]['properties']['description']
                        nws_icon = 16701
            except:
                nws_alert_headline = county_code #data['title']
                nws_alert_description = "There are no active watches, warnings or advisories"
                nws_icon = 46935
    else:
        nws_alert_headline = data['features'][0]['properties']['headline']
        nws_alert_description = data['features'][0]['properties']['description']
        nws_icon = 16701    

    frame_duration = len(nws_alert_description.split()) / 4 + 2
    api_response = {
        "frames": [
            {
                "text": "Alert Headline: "+ str(nws_alert_headline),
                "icon": int(nws_icon),
                "duration": int(frame_duration)
            },
            {
                "text": "Alert Description: " + str(nws_alert_description),
                "icon": int(nws_icon),
                "duration": int(frame_duration)
            }
            ]
        
    }
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)

    return response_object