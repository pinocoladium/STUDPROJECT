import requests
import json

def comparison_hero(link, hero_list):
    uri = link + '/all.json'
    responce = requests.get(uri)
    dict_local = {}
    for hero in json.loads(responce.text):
        for name_hero in hero_list:
            if name_hero == hero['name']:
                dict_local[hero['powerstats']['intelligence']] = hero['name']
            else:
                continue
    
    intl, name = sorted(dict_local.items())[-1]

    return print(f'The smartest superhero on this list - {name}, his intelligence is - {intl}')


# comparison_hero('https://akabab.github.io/superhero-api/api', ['Thanos', 'Hulk', 'Captain America'])


class Yandex:
    
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_file(self, path_to_file):
        urn = 'v1/disk/resources/upload/'
        uri = self.url + urn
        params = {'path': f'/{path_to_file}'}
        link = requests.get(uri, headers=self.get_headers(), params=params)
        full_link = link.json()['href']
        response = requests.put(full_link, headers=self.get_headers(), data=open(path_to_file, 'rb'))
        if response.status_code == 201:
            print('Uploaded successfully')


# token = input('To connect, enter your OAuth token: ')
# yan = Yandex(token)
# yan.get_upload_file('test.txt')


def get_questions_stackoverflow(tags):
    dict_link = {}
    uri = 'https://api.stackexchange.com/2.3/questions?fromdate=1670716800&todate=1670889600&site=stackoverflow'
    responce = requests.get(uri)
    for el in json.loads(responce.text)['items']:
        if tags in el['tags']:
            dict_link[el['title']] = el['link']
    
    return print(dict_link)
    

# get_questions_stackoverflow('python')