import requests

def lambda_handler(event, context):
    api_url = 'https://api.yomomma.info/'
    response = requests.get(api_url, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if response.status_code == requests.codes.ok:
        return(response.text)
    else:
        return("Error:", response.status_code, response.text)
