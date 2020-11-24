#!/usr/bin/python3

import os
import random
import time

from pamfax import PamFax

# Either configure it manually or by using an external config.py file
if os.path.isfile('./config.py'):
    from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET
else:
    HOST = 'api.pamfax.biz'  # Either (testing) sandbox-api.pamfax.biz OR (production) api.pamfax.biz
    USERNAME = 'your PamFax username here'
    PASSWORD = 'your PamFax password here'
    APIKEY = 'your PamFax API key here'
    APISECRET = 'your PamFax API secret word here'


def _assert_json(response):
    assert response['result']['code'] == 'success'


if __name__ == "__main__":

    print('Welcome to the PamFax Python 3 Sample by using the a1pamfax package\n')
    print('Host: ' + HOST)
    print('Username: ' + USERNAME)
    print('API Key: ' + APIKEY)

    print("\nLogin with PamFax credentials..")
    pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)

    print("Creating a fax with cover..")
    response = pamfax.create()
    _assert_json(response)
    response = pamfax.list_available_covers()
    _assert_json(response)
    response = pamfax.set_cover(response['Covers']['content'][1]['id'], 'My test fax with PamFax using Python3')
    _assert_json(response)

    print("Adding a random recipient..")
    rnd_phone = str(random.randint(10000000, 99999999))  # Berlin has 8 digits after 030..
    response = pamfax.add_recipient('+49030' + rnd_phone)
    _assert_json(response)

    print("Waiting until fax is ready to send..")
    while True:
        response = fax_state = pamfax.get_state()
        _assert_json(response)
        # print(fax_state['FaxContainer']['state'])
        if fax_state['FaxContainer']['state'] == 'ready_to_send':
            break
        time.sleep(2)

    print("Fax setup done, sending..")
    response = pamfax.send()
    _assert_json(response)

    input("\nPress ENTER twice to exit")
