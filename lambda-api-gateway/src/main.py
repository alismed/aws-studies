import requests

def lambda_handler(event, context):
    api_url = 'https://v6.exchangerate-api.com/v6/'

    amount       = event['queryStringParameters']['amount']
    fromCurrency = event['queryStringParameters']['fromCurrency']
    toCurrency   = event['queryStringParameters']['toCurrency']
    apikey       = event['queryStringParameters']['key']

    api_url += apikey + '/pair/' + fromCurrency + '/' + toCurrency + '/' + str(amount)
    response = requests.get(api_url, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if response.status_code == requests.codes.ok:
        return(response.text)
    else:
        return("Error:", response.status_code, response.text)
