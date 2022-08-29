import pytest
import requests
from main import create_folder_yd, ya_token

FIXTURE_create_folder_yd_1 = [
    (ya_token, 'Test001', '<Response [201]>', True),
    (ya_token, 'Test002/test_2', '<Response [201]>', True),
    (ya_token, 'Test003', '<Response [201]>', False),
    (ya_token, 'Test003', '<Response [409]>', True),
    (ya_token, 'Test004;:', '<Response [400]>', False),
    ('FalseToken 404', 'Test004;:', '<Response [401]>', False)
]
FIXTURE_create_folder_yd_2 = [
    (ya_token, 'Test001/test_2', '<Response [200]>', True)
]

@pytest.mark.parametrize('token, adres, result, delete', FIXTURE_create_folder_yd_1)
def test_create_folder_yd_1(token, adres, result, delete):
    #TODO 01. Тестирование создания папки
    assert str(create_folder_yd(token, adres)) == result

    #TODO 02. Удаление созданной тестовой папки
    if delete:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}
        folder_path_list = adres.split('/')
        params = {'path': folder_path_list[0]}
        requests.delete(url, headers=headers, params=params)

@pytest.mark.parametrize('token, adres, result, delete', FIXTURE_create_folder_yd_2)
def test_create_folder_yd_2(token, adres, result, delete):
    #TODO 01. Тестирование создания папки var 2
    create_folder_yd(token, adres)

    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}
    params = {'path': adres}
    assert str(requests.get(url, headers=headers, params=params)) == result

    #TODO 02. Удаление созданной тестовой папки
    if delete:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}
        folder_path_list = adres.split('/')
        params = {'path': folder_path_list[0]}
        requests.delete(url, headers=headers, params=params)
