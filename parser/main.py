import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"

def _get_headers():
    return Headers(browser="firefox", os="win").generate()

def _get_text(url):
    return requests.get(url, headers=_get_headers()).text


words = ['Django', 'Flask']


def get_vacancy(word_list, url):
    bs = BeautifulSoup(_get_text(url), features='html5lib')
    vac_list = bs.find(class_="vacancy-serp-content")
    vac_tag = vac_list.find_all(class_="serp-item")
    vac_dict = {}
    for word in word_list:
        n = 1
        for el in vac_tag:
            title = el.find_all(class_="bloko-header-section-3")[0].text
            link = el.find(class_="serp-item__title")['href']
            salary = el.find_all(class_="bloko-header-section-3")[1].text
            location = el.find_all(class_='bloko-text')[1].text
            company = el.find_all(class_='bloko-text')[0].text
            if word in title:
                vac_dict[f'vacancy {n}'] = {
                    'title': title,
                    'link': link,
                    'salary': salary,
                    'location': location,
                    'company': company
                }
                n += 1
    
    with open('vacancy.json', 'w', encoding='utf-8') as f:
        json.dump(vac_dict, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    get_vacancy(words, HOST)