import unittest
from unittest import TestCase
from main import geo_filter
from main import get_unique_id
from main import ids
from main import get_highest_stats


class GeofilterTestCase(TestCase):

    def test_with_right_structure(self):
        data = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']}]
        self.assertIsInstance(data, list)
        for i in data:
            self.assertIsInstance(i, dict)

    @unittest.expectedFailure
    def test_titles(self):
        data = geo_filter([{'visit1': ['Москва', 'Россия']},
                           {'visit2': ['пермь', 'россия']}])
        res = [{'visit1': ['Москва', 'Россия']},
               {'visit2': ['пермь', 'россия']}]
        self.assertEqual(data, res)

    def test_English(self):
        data = geo_filter([{'visit1': ['Москва', 'Россия']},
                           {'visit2': ['Moscow', 'Russia']}])
        res = [{'visit1': ['Москва', 'Россия']},
               {'visit2': ['Moscow', 'Russia']}]
        self.assertEqual(data, res)


class UniqueIdTestCase(TestCase):
    def test_len_unique(self):
        expected = len(get_unique_id(ids))
        data = len(set(get_unique_id(ids)))
        self.assertEqual(data, expected)


class GetHighestTestCase(TestCase):
    def test_highest(self):
        data = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        res = get_highest_stats(data)
        for value in data.values():
            self.assertLessEqual(value, data[res])
