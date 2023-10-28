import unittest
import requests

import pytest

import sys

sys.path.append(r"C:\Users\1\Desktop\REP\TESTS")
from main import get_list_visits, get_unique_id, get_dict_in_dict, create_folder_yandisk


class TestGet_list_visits(unittest.TestCase):
    def test_key_in_dict(self):
        key = "visit"
        list_ = get_list_visits()
        for el in list_:
            self.assertIn(key, str(el.keys()))

    @unittest.expectedFailure
    def test_value_in_dict(self):
        word = "Россия"
        list_ = get_list_visits()
        for el in list_:
            self.assertNotIn(word, str(el.values()))

    def test_len_values(self):
        list1 = ["Курск", "Россия"]
        list_ = get_list_visits()
        for el in list_:
            for value in el.values():
                self.assertEqual(len(list1), len(value))


class TestGet_unique_id:
    def test_unique(self):
        list_ = get_unique_id()
        list_unique = set(list_)
        assert len(list_) == len(list_unique)

    @pytest.mark.parametrize("summ", [213, 15, 54, 119, 98, 35])
    def test_summ(self, summ):
        sum_list = sum(get_unique_id())
        assert summ < sum_list

    def test_int(self):
        list_ = get_unique_id()
        for el in list_:
            assert type(el) == int


class TestGet_dict_in_dict(unittest.TestCase):
    def test_dict(self):
        dict_ = get_dict_in_dict()
        value_dict = dict_.values()
        self.assertEqual(type(dict_), dict)

    def test_value_dict(self):
        dict_ = get_dict_in_dict()
        value_dict = dict_.values()
        for el in value_dict:
            self.assertEqual(type(el), dict)

    @unittest.expectedFailure
    def test_equal_list(self):
        dict_ = get_dict_in_dict()
        for el1 in value_dict:
            for el2 in el1:
                for el3 in el2:
                    for el4 in el3:
                        self.assertEqual(type(el4), list)


class TestCreate_folder_yandisk(unittest.TestCase):
    def test_code_responce(self):
        responce = create_folder_yandisk()
        code = responce.status_code
        expected = 201
        self.assertEqual(code, expected)

    @unittest.expectedFailure
    def test_code_responce_negative(self):
        responce = create_folder_yandisk()
        code = responce.status_code
        expected = 201
        self.assertNotAlmostEqual(code, expected)

    def test_get_info(self):
        name_folder = "new folder"
        create_folder_yandisk(name_folder=name_folder)
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        token = "....."
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {token}",
        }
        params = {"path": f"/{name_folder}"}
        code = requests.get(url, headers=headers, params=params).status_code
        expected = 200
        self.assertEqual(code, expected)


# python -m unittest tests/test_main.py
# python -m pytest
