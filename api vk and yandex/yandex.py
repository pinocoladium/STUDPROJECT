import requests
import json
from progress.bar import IncrementalBar

bar = IncrementalBar('overall progress', max = 3)

class Yandex:
    
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, name_folder):
        urn = 'v1/disk/resources/'
        url = self.url + urn
        params = {'path': name_folder}
        response = requests.put(url, headers=self.get_headers(), params=params)

    def upload_from_vk(self, list_photos, name_folder='photos vk'):
        bar = IncrementalBar('Yandex Progress', max = 2)
        if list_photos == None:
            print('No photo. Loading is not possible')
            return
        else:
            bar.next()
            print(' - Photo loading in progress....')
            urn = 'v1/disk/resources/upload/'
            url = self.url + urn
            self.create_folder(name_folder)
            for el in list_photos:
                url_photos = el['url_photos']
                file_name = el['names']
                params = {'path': f'/{name_folder}/{file_name}', 'url': url_photos}
                response = requests.post(url, headers=self.get_headers(), params=params)
            if response.status_code == 202:
                bar.next()
                print(' - Photo successfully uploaded to Yandex.Disk')
            else:
                print('Photo not uploaded. An error has occurred')
            return

