#!/usr/bin/python

# XtendOps timekeeping script - https://xconnect.xtendops.com/dashboard/timekeeping
# Author: Kleo Bercero - https://github.com/kleo / kleo@hak.dog

import requests
import json

headers = {
    'host': 'staging-api.xtendops.com',
    'content-length': '40',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'content-type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://xconnect.xtendops.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://xconnect.xtendops.com/',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
}

credentials = {
    'uid': '<username>',
    'password': '<password>',
}

login = requests.post('https://staging-api.xtendops.com/auth/login', headers=headers, json=credentials)

a = json.loads(login.text)

headers2 = {
    'authority': 'staging-api.xtendops.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer ' + a['accessToken'],
    'origin': 'https://xconnect.xtendops.com',
    'referer': 'https://xconnect.xtendops.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36',
}

response1 = requests.get('https://staging-api.xtendops.com/auth', headers=headers2)

b = json.loads(response1.text)

json_data2 = {
    'accountId': b['profile']['id'],
    'hostname': 'xconnect.xtendops.com',
}

response2 = requests.post('https://staging-api.xtendops.com/timekeeping/attendance/login', headers=headers2, json=json_data2)

c = json.loads(response2.text)

# Login Time: 2022-12-07T11:56:49.000Z - Success: True - ID: 367189
print('Login Time:', c['attendanceLog']['dtr']['loginTime'], '-', 'Success:', c['success'], '-', 'ID:', c['attendanceLog']['dtr']['id'])