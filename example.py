#!/usr/bin/python3

from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET, DROPBOX_USERNAME, DROPBOX_PASSWORD
from pamfax import PamFax

response = pamfax.get_current_settings()
print(response)
