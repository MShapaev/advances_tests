ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98
         }


def geo_filter(list):
    return [i for i in list for j in i.values() if 'Россия' in j or 'Russia' in j]


def get_unique_id(some_dict):
    return list(set([j for i in some_dict for j in some_dict[i]]))


def get_highest_stats(some_dict):
    return sorted(some_dict.items(), key=lambda value: value[1])[-1][0]


def main():

    geo_filter(geo_logs)
    get_unique_id(ids)
    get_highest_stats(stats)



if __name__ == '__main__':
    main()
