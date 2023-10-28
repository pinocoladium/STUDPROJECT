from pprint import pprint
from collections import defaultdict
import csv
import re

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

words_list = []

for el in contacts_list:
    text = str(el)
    text = text.replace(", ''", '').replace(" , ", ' ').replace('[', '').replace(']', '')
    words_str = re.sub(r"'(\w+)\s(\w+)(\s(\w+(вич|вна)))?'", r"'\1', '\2', '\3'", text)
    pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s*-?(\d{3})-?(\d{2})(-?(\d{2}))((\s?)\(?(доб.)??\s*(\d{4})\))?"
    result_str = re.sub(pattern, r"+7(\2)\3-\4-\6\8\9\10", words_str)
    result_str = result_str.replace("'", '').replace(' , ', ' ').replace('  ', ' ').replace(', ', ',')
    result = result_str.split(',')
    words_list.append(result)

data = defaultdict(list)

for info in words_list:
    key = tuple(info[:2])
    for item in info:
        if item not in data[key]:
            data[key].append(item)

result_list = list(data.values())

with open("phonebook.csv", "w", encoding='utf8') as f:
  datawriter = csv.writer(f)
  datawriter.writerows(result_list)

