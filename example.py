#!/usr/bin/python3

from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET, DROPBOX_USERNAME, DROPBOX_PASSWORD
from pamfax import PamFax
from pprint import pprint

pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)
response = pamfax.get_current_settings()
pprint(response)
