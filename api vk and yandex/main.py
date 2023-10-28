import json
from progress.bar import IncrementalBar
from yandex import Yandex
from vk import Vk

token_vk = input('Enter your service code or OAuth token VK: ')
token_yan = input('Enter your OAuth token Yandex: ')
id = input('Enter account id in VK: ')


if __name__ == '__main__':

    bar = IncrementalBar('Overall progress', max = 3)
    vk_client = Vk(token_vk, '5.131')
    yan = Yandex(token_yan)
    
    result = vk_client.get_photos(id)
    bar.next()
    print(' - Vk function completed')
    
    yan.upload_from_vk(result)
    bar.next()
    print(' - Yandex function completed')
    
    if result != None:
        bar.next()
        print(' - Output information into info.json')
        with open ('info.json', 'wt',  encoding='utf-8') as file_json:
            info = []
            for el in result:
                info.append({'file_name': f'{el["names"]}.jpg', 'size': el["size"]})
            json.dump(info, file_json, indent=2)
            
    else:
        print('Information in the info.json is not included')
    

