from logger1 import logger
from logger2 import logger_with_param


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

@logger
def flat_generator(list_of_lists):
    for el in list_of_lists:
        for item in el:
            yield item
            
@logger_with_param('main_2.log')
def flat_generator_2(list_of_lists):
    for el in list_of_lists:
        for item in el:
            yield item

flat_generator(list_of_lists_1)
flat_generator_2(list_of_lists_1)