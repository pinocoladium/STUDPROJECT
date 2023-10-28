import requests
import json
from progress.bar import IncrementalBar

class Vk:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {'access_token': token, 'v': version}
    def get_photos(self, id, count=5):
        bar = IncrementalBar('Vk progress', max = 3)
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {'album_id': 'profile', 'owner_id': id, 'extended': 1, 'count': count}
        res = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        if "error" in res.keys():
            print('Error')
            return
        elif "error" in res.keys() and int(res["error"]["error_code"]) == 30:
            print('This profile is private. Information is not available')
            return
        elif int(res["response"]["count"]) == 0:
            print('Photo not found. Profile has no photo')
            return 
        else:
            bar.next()
            print(f' - Found {res["response"]["count"]} photos')
            bar.next()
            print(' - Getting information about a photo....')
        list_photos = []
        list_likes = []
        for el in (res['response']['items']):
            likes = el['likes']['count']
            s = el['date']
            import time
            date = time.strftime('%d.%m.%y', time.gmtime(s))
            size = el['sizes'][-1]['type']
            url_photos = el['sizes'][-1]['url']
            if likes not in list_likes:
                name = likes
            if likes in list_likes:
                name = f'{likes} - {date}'
            list_likes.append(likes)
            list_photos.append({'names': name, 'likes': likes, 'date': date, 'size': size, 'url_photos': url_photos})
        bar.next()
        print(' - Photo information received....')
            
        return list_photos



