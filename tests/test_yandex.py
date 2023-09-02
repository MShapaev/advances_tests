from unittest import TestCase
from yandex import create_folder
import requests
from yandex import URL, headers
from keys import TOKEN


class CreateFolderTestCase(TestCase):

    def test_connection(self):
        code, path = create_folder('TEST')
        bad_codes = [400, 401, 403, 303, 406, 413, 423, 429, 503, 507]
        self.assertNotIn(code, bad_codes)

    def test_with_right_response(self):
        code, path = create_folder('TEST')
        expecting = [409, 201]
        self.assertIn(code, expecting)

    def test_folder_in_yandex(self):
        code, path = create_folder('TEST')
        res = requests.get(f'{URL}?path={path}', headers=headers)
        code = res.status_code
        expect = 200
        self.assertEqual(code, expect)
