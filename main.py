import requests #Библиотека для работы с api
from pprint import pprint

ya_token = '' # TODO Введите Ваш токен
folder_path = '04_ProfPy/RazrTestDZ_2aghadfh'

def create_folder_yd_i(ya_token, folder_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + ya_token}
    params = {'path': folder_path}
    return requests.put(url, headers=headers, params=params)

def create_folder_yd(ya_token, folder_path):
    if '/' in folder_path:
        folder_path_list = folder_path.split('/')
        fold_p_i = folder_path_list[0]
        create_folder_yd_i(ya_token, fold_p_i)
        for i_1 in range(1, len(folder_path_list)):
            fold_p_i = fold_p_i + '/' + folder_path_list[i_1]
            ans = create_folder_yd_i(ya_token, fold_p_i)
    else:
        ans = create_folder_yd_i(ya_token, folder_path)
    return ans

def delete_folder_yd(ya_token, folder_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + ya_token}
    params = {'path': folder_path}
    return requests.delete(url, headers=headers, params=params)

def folder_status(ya_token, folder_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + ya_token}
    params = {'path': folder_path}
    return requests.get(url, headers=headers, params=params)


if __name__ == '__main__':
    # print(create_folder_yd(ya_token, folder_path))
    #print(delete_folder_yd(ya_token, folder_path))
    #pprint(folder_status(ya_token, folder_path))
