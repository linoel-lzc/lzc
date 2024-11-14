import requests
from ip_list import list_ip


# def upgrades(ip, files):
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
#                "Content-Type": "application/x-www-form-urlencoded"}
#     datas = {"387": files}
#
#     url = f'http://{ip}/admin/acisco.csc'
#     response = requests.post(url=url, headers=headers, data=datas)
#     return response.status_code
#
#
# if __name__ == '__main__':
#     ip_list = list_ip('ip_list')
#     print(ip_list)
#     # if ever used
#     # file = ""
#     # for i in ip_list:
#     #     try:
#     #         status = upgrades(i, file)
#     #         print(status)
#     #     except Exception as a:
#     #         print(a)
#     file = "http://10.74.62.106:6970/a.xml"
#     for i in ip_list:
#         try:
#             status = upgrades(i, file)
#             print('---------------------------------------------------------------------')
#             print('{} upgrade success,status code is {}'.format(i, status))
#         except Exception as a:
#             print('{} upgrade failed'.format(i))
#             continue

def upgrades(ip, files):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
               "Content-Type": "application/x-www-form-urlencoded"}
    datas = {"410": files}

    url = f'http://{ip}/admin/acisco.csc'
    response = requests.post(url=url, headers=headers, data=datas)
    return response.status_code


if __name__ == '__main__':
    ip_list = list_ip('ip_list')
    print(ip_list)
    file = "http://10.74.128.199/phoneloads/PHONEOS.3-2-1-0001-73dev.loads"
    file1 = ' '
    for i in ip_list:
        try:
            status = upgrades(i, file)
            print('---------------------------------------------------------------------')
            print('{} upgrade success,status code is {}'.format(i, status))
        except Exception as a:
            print('{} upgrade failed'.format(i))
            continue



