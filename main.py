import requests
from pprint import pprint
def get_user_info():
    #response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()
    TOKEN = '1397099411.1436082.205d096159f742f0ae5b7d80389ef7cd'
    BASE_URL = 'https://api.instagram.com/v1'
    END_POINT = '/users/self'

    ACCESS_TOKEN = '?access_token={token}'.format(token=TOKEN)

    user_info = requests.get(BASE_URL+END_POINT+ACCESS_TOKEN).json()

    pprint (user_info)

get_user_info()