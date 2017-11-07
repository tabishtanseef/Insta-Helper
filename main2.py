import requests
BASE_URL = 'https://api.instagram.com/v1'
response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN = response['access_token']
print APP_ACCESS_TOKEN
def self_info():
    request_url = (BASE_URL + '/users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url)

    if user_info.status_code == 200:
        print user_info.json()
    else:
        print 'Status code other than 200 received!'


self_info()