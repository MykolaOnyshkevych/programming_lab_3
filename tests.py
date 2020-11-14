import unittest
from wedding import wedding_graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.first_list_from_example = [(1, 2), (2, 4), (3, 5)]
        self.second_list_from_example = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        self.first_resault = 4
        self.second_resault = 6

    def test_first_list_from_example(self):
        self.assertEqual(wedding_graph(len(self.first_list_from_example), self.first_list_from_example), self.first_resault)

    def test_second_list_from_example(self):
        self.assertEqual(wedding_graph(len(self.second_list_from_example), self.second_list_from_example), self.second_resault)


if __name__ == '__main__':
    unittest.main()