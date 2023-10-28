import requests


def get_list_visits(country="Россия"):
    geo_logs = [
        {"visit1": ["Москва", "Россия"]},
        {"visit2": ["Дели", "Индия"]},
        {"visit3": ["Владимир", "Россия"]},
        {"visit4": ["Лиссабон", "Португалия"]},
        {"visit5": ["Париж", "Франция"]},
        {"visit6": ["Лиссабон", "Португалия"]},
        {"visit7": ["Тула", "Россия"]},
        {"visit8": ["Тула", "Россия"]},
        {"visit9": ["Курск", "Россия"]},
        {"visit10": ["Архангельск", "Россия"]},
    ]

    other_visits = []
    for id, my_dict in enumerate(geo_logs):
        for keys, values in my_dict.items():
            if f"{country}" not in values:
                other_visits.append(id)

    cycle = 0
    for other_visits_id in other_visits:
        del geo_logs[other_visits_id - cycle]
        cycle += 1

    return geo_logs


def get_unique_id():
    ids = {
        "user1": [213, 213, 213, 15, 213],
        "user2": [54, 54, 119, 119, 119],
        "user3": [213, 98, 98, 35],
    }

    unique_id = []

    for values in ids.values():
        for id in set(values):
            if id not in unique_id:
                unique_id.append(id)
    print(unique_id)
    return unique_id


def get_dict_in_dict():
    my_list = [
        78,
        "kkkk",
        "2018-01-01",
        "yandex",
        "cpc",
        100,
        "2018-01-01",
        "yandex",
        "cpc",
        100,
        45,
    ]

    my_dict = my_list[-1]

    for el in reversed(my_list[:-1]):
        my_dict = {el: my_dict}

    return my_dict


def create_folder_yandisk(name_folder="new folder"):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    token = "...."
    headers = {"Content-Type": "application/json", "Authorization": f"OAuth {token}"}
    params = {"path": f"/{name_folder}"}
    response = requests.put(url, headers=headers, params=params)
    return response
