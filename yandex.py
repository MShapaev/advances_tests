import requests
from keys import TOKEN

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    res = requests.put(f'{URL}?path={path}', headers=headers)
    return res.status_code, path


def main():
    create_folder('TEST')


if __name__ == '__main__':
    main()
