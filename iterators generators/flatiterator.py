class FlatIterator:

    def __init__(self, list_of_list):
         self.len_list = len(list_of_list)
         self.list_of_list = list_of_list

    def __iter__(self):
        self.counter1 = 0
        self.counter2 = 0
        return self

    def __next__(self):
        if self.counter1 == (self.len_list) and self.counter2 == 0:
            raise StopIteration
        item = self.list_of_list[self.counter1][self.counter2]
        if self.counter2 == (len(self.list_of_list[self.counter1]) - 1):
            self.counter1 += 1
            self.counter2 = 0
        else:
            self.counter2 += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()