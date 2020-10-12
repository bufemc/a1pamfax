#!/usr/bin/python3

import os.path
import time

from pamfax import PamFax

# Either configure it manually or by using an external config.py file
if os.path.isfile('./config.py'):
    from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET
else:
    HOST = 'api.pamfax.biz'  # Either sandbox-api.pamfax.biz OR api.pamfax.biz
    USERNAME = 'standard pamfax account username from live/sandbox'
    PASSWORD = 'standard pamfax account password'
    APIKEY = 'your API key here'
    APISECRET = 'your API secret word'

print('Welcome to PamFax Python 3 Sample\n')
print('Host: ' + HOST)
print('Username: ' + USERNAME)
print('API Key: ' + APIKEY)
# print('API Secret: ' + APISECRET)

pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)

pamfax.create()

response = pamfax.list_available_covers()
# last cover
# print(response['Covers']['content'][-1])

# print "\n\nAdding cover:\n"
response = pamfax.set_cover(response['Covers']['content'][-1]['id'], 'My test fax with PamFax using Python')
# use response['Covers']['content'][1]['id'] for first or see all covers in pamfax.list_available_covers() result
# print(response)

# print "\n\nAdding recipient:\n"
response = pamfax.add_recipient('add number here, example +12345678')
# print(response)

# print "\n\nWaiting, while fax preparing...\n"
# time.sleep(10)

while True:
    fax_state = pamfax.get_fax_state()
    if fax_state['FaxContainer']['state'] == 'ready_to_send':
        break
    time.sleep(2)

print("\n\ndone, sending...\n")

response = pamfax.send()

print(response)

input('click any key to exit')
