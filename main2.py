import requests
from pprint import pprint
BASE_URL = 'https://api.instagram.com/v1'
response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN = response['access_token']


def self_info():
    request_url = (BASE_URL + '/users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        pprint (user_info['data']['full_name'])
    else:
        print 'Status code other than 200 received!'


self_info()