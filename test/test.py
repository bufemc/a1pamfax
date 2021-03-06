#!/usr/bin/python3

import logging
import os
import random
import socket
import sys
import time
import unittest

develop_mode = False
if (develop_mode):
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Find config and pamfax when no Package
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'pamfax'))  # Find processors when no Package

from pamfax import PamFax

try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET, DROPBOX_USERNAME, DROPBOX_PASSWORD
except:
    raise Exception('Copy config.example.py to config.py and adapt with your credentials first!')

IP_ADDR = socket.gethostbyname('www.airport1.de')

"""
Make sure to upload a file through

     https://sandbox-api.pamfax.biz/server/faxin/faxintest.php

before running this test.

Update 2020: This form seems to be outdated and may not work anymore as expected.
It's better you really send a fax to yourself (to your phone number, which should
be registered at PamFax), or ask s.o. at PamFax to do it for you?
That's why I changed the test code to proceed also if no faxes are in your inbox!

If you want to run the OnlineStorage tests you also have to authenticate yourself first
in a browser as described here:

    https://sandbox-apifrontend.pamfax.biz/processors/onlinestorage/
    
Do not forget to provide the usertoken, given e.g. by the method VerifyUser:

    https://api.pamfax.biz/OspAuth/DropboxStorage?usertoken=xxx

"""

# Set to either WARNING or DEBUG (warning: very much output!)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pamfax')


def _assert_json(message, response, check_response=True):
    logger.debug(message)
    logger.debug(response)
    if check_response:
        assert response['result']['code'] == 'success'
    logger.debug('*' * 10)
    return response


def _assert_file(message, f, content_type):
    logger.debug(message)
    logger.debug(content_type)
    assert f is not None
    assert content_type is not None


# Seed our test account with credit and a fax
pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)

message = 'Adding credit to sandbox user'
response = pamfax.add_credit_to_sandbox_user(1000, "Testing purposes")
_assert_json(message, response)

message = 'Listing inbox faxes'
response = pamfax.list_inbox_faxes()
_assert_json(message, response)

if 'content' not in response['InboxFaxes']:
    print("You have no faxes in your inbox - provide them first")
    file_uuid = None
    uuid = None
else:
    files = response['InboxFaxes']['content']
    f = files[0]
    file_uuid = f['file_uuid']
    uuid = f['uuid']


class TestPamFax(unittest.TestCase):
    """A set of unit tests for this implementation of the PamFax API."""

    # https://sandbox-apifrontend.pamfax.biz/processors/common/
    def test_Common(self):

        # New methods not implemented by dynaptico
        message = 'Getting currency by language code'
        response = pamfax.get_currency_by_lang('DE')
        _assert_json(message, response)

        message = 'Getting current culture info'
        response = pamfax.get_current_culture_info()
        _assert_json(message, response)

        message = 'Getting formatted price'
        response = pamfax.get_formatted_price('127.0.0.1')
        _assert_json(message, response)

        message = 'Listing cities'
        response = pamfax.list_cities('DEU')
        _assert_json(message, response)

        message = 'Listing countries prices'
        response = pamfax.list_countries_prices('EN')
        _assert_json(message, response)

        message = 'Listing country states'
        response = pamfax.list_country_states('US')
        _assert_json(message, response)

        message = 'Listing destinations for zone'
        response = pamfax.list_destinations_for_zone('1')
        _assert_json(message, response)

        message = 'Listing zip codes'
        response = pamfax.list_zip_codes('DEU', 'Berlin')
        _assert_json(message, response)

        message = 'Setting culture'
        response = pamfax.set_culture('DE')
        _assert_json(message, response)

        message = 'Getting current settings'
        response = pamfax.get_current_settings()
        _assert_json(message, response)

        # ToDo: find a solution to have at least 1 fax in inbox for the tests
        if file_uuid:
            message = 'Getting file'
            f, content_type = pamfax.get_file(file_uuid)
            _assert_file(message, f, content_type)

        message = 'Getting geo IP information'
        response = pamfax.get_geo_ip_information(IP_ADDR)
        _assert_json(message, response)

        # ToDo: find a solution to have at least 1 fax in inbox for the tests
        if uuid:
            message = 'Getting page preview'
            f, content_type = pamfax.get_page_preview(uuid, 1)
            _assert_file(message, f, content_type)

        message = 'Listing countries'
        response = pamfax.list_countries()
        _assert_json(message, response)

        message = 'Listing countries for zone'
        response = pamfax.list_countries_for_zone(1)
        _assert_json(message, response)

        message = 'Listing currencies 1'
        response = pamfax.list_currencies()
        _assert_json(message, response)

        message = 'Listing currencies 2'
        response = pamfax.list_currencies('JPY')
        _assert_json(message, response)

        message = 'Listing languages 1'
        response = pamfax.list_languages()
        _assert_json(message, response)

        message = 'Listing languages 2'
        response = pamfax.list_languages(50)
        _assert_json(message, response)

        message = 'Listing strings'
        response = pamfax.list_strings(['hello'])
        _assert_json(message, response)

        message = 'Listing supported file types'
        response = pamfax.list_supported_file_types()
        _assert_json(message, response)

        message = 'Listing timezones'
        response = pamfax.list_timezones()
        _assert_json(message, response)

        message = 'Listing versions'
        response = pamfax.list_versions()
        _assert_json(message, response)

        message = 'Listing zones'
        response = pamfax.list_zones()
        _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/faxhistory/
    def test_FaxHistory(self):
        message = 'Adding note to fax'
        response = pamfax.add_fax_note(uuid, 'This is my favorite fax')
        _assert_json(message, response)

        message = 'Counting faxes'
        response = pamfax.count_faxes('inbox')
        _assert_json(message, response)

        message = 'Deleting faxes'
        response = pamfax.delete_faxes([uuid])
        _assert_json(message, response)

        # Will work only once of course, then will message: fax_not_found
        # message = 'Deleting faxes for period'
        # response = pamfax.delete_faxes_for_period('inbox', '2020-01-01', '2020-01-31')
        # _assert_json(message, response)

        # message = 'Deleting faxes for recipient number'
        # response = pamfax.delete_from_list_recent_recipients('123456')
        # _assert_json(message, response)

        message = 'Restoring fax'
        response = pamfax.restore_fax(uuid)
        _assert_json(message, response)

        # message = 'Deleting faxes from trash'
        # response = pamfax.delete_faxes_from_trash([uuid])
        # _assert_json(message, response)

        message = 'Emptying trash'
        response = pamfax.empty_trash()
        _assert_json(message, response)

        message = 'Getting fax details'
        response = pamfax.get_fax_details(uuid)
        _assert_json(message, response)

        # message = 'Getting fax group'
        # response = pamfax.get_fax_group(uuid)
        # _assert_json(message, response)

        message = 'Getting inbox fax'
        response = pamfax.get_inbox_fax(uuid, mark_read=False)
        _assert_json(message, response)

        # message = 'Listing fax group'
        # response = pamfax.list_fax_group(uuid)
        # _assert_json(message, response)

        message = 'Listing fax notes'
        response = pamfax.list_fax_notes(uuid)
        _assert_json(message, response)

        message = 'Listing inbox fax'
        response = pamfax.list_inbox_fax()
        _assert_json(message, response)

        message = 'Listing inbox faxes'
        response = pamfax.list_inbox_faxes()
        _assert_json(message, response)

        message = 'Listing outbox faxes'
        response = pamfax.list_outbox_faxes()
        _assert_json(message, response)

        message = 'Listing recent faxes'
        response = pamfax.list_recent_faxes()
        _assert_json(message, response)

        message = 'Listing recent recipients'
        response = pamfax.list_recent_recipients()
        _assert_json(message, response)

        message = 'Listing sent faxes'
        response = pamfax.list_sent_faxes()
        _assert_json(message, response)

        out_uuid = response['SentFaxes']['content'][0]['uuid']

        message = 'Getting transmission report'
        f, content_type = pamfax.get_transmission_report(out_uuid)
        _assert_file(message, f, content_type)

        # message = 'Listing trash'
        # response = pamfax.list_trash()
        # _assert_json(message, response)

        message = 'Listing unpaid faxes'
        response = pamfax.list_unpaid_faxes()
        _assert_json(message, response)

        message = 'Publishing a fax'
        response = pamfax.publish_fax(uuid)
        _assert_json(message, response)

        message = 'Getting data for published fax'
        response = pamfax.get_published_fax(uuid)
        _assert_json(message, response)

        message = 'Unpublishing a fax'
        response = pamfax.unpublish_fax(uuid)
        _assert_json(message, response)

        message = 'Setting fax as read'
        response = pamfax.set_fax_read(uuid)
        _assert_json(message, response)

        message = 'Setting faxes as read'
        response = pamfax.set_faxes_as_read([uuid])
        _assert_json(message, response)

        message = 'Setting spam state for faxes'
        response = pamfax.set_spam_state_for_faxes([uuid], is_spam=False)
        _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/faxjob/
    def test_FaxJob(self):
        message = 'Creating a fax job'
        response = pamfax.create()
        _assert_json(message, response)

        message = 'Listing available covers'
        response = pamfax.list_available_covers()
        _assert_json(message, response)

        message = 'Adding a cover'
        response = pamfax.set_cover(response['Covers']['content'][1]['id'], 'Dynaptico: Tomorrow On Demand')
        _assert_json(message, response)

        message = 'Adding a remote file'
        response = pamfax.add_remote_file('https://s3.amazonaws.com/dynaptico/Dynaptico.pdf')
        _assert_json(message, response)

        message = 'Adding a local file'
        filepath = os.path.join(os.path.dirname(__file__), 'Dynaptico.pdf')
        response = pamfax.add_file(filepath)
        _assert_json(message, response)

        message = 'Removing a file'
        response = pamfax.remove_file(response['FaxContainerFile']['file_uuid'])
        _assert_json(message, response)

        message = 'Adding recipient 1'
        rnd_phone = str(random.randint(10000000, 99999999))
        response = pamfax.add_recipient('+49030' + rnd_phone)
        _assert_json(message, response)

        message = 'Adding recipient 2'
        rnd_phone = str(random.randint(10000000, 99999999))
        response = pamfax.add_recipient('+49030' + rnd_phone)
        _assert_json(message, response)

        message = 'Removing a recipient'
        response = pamfax.remove_recipient(response['FaxRecipient']['number'])
        _assert_json(message, response)

        message = 'Listing recipients'
        response = pamfax.list_recipients()
        _assert_json(message, response)

        message = 'Listing fax files'
        response = pamfax.list_fax_files()
        _assert_json(message, response)

        # Check state
        logger.debug('*' * 10)
        logger.debug('Checking state')
        t = 0
        while True:
            fax_state = pamfax.get_state()
            logger.debug(fax_state)
            if fax_state['FaxContainer']['state'] == 'ready_to_send':
                break
            time.sleep(2)
            t += 2
            logger.debug("%d seconds elapsed...", t)
        assert fax_state['FaxContainer']['state'] == 'ready_to_send'

        message = 'Preview the fax'
        response = pamfax.get_preview()
        _assert_json(message, response)

        message = 'Send the fax'
        response = pamfax.send()
        _assert_json(message, response)

        # This only works if you don't have enough credit now
        # message = 'Send the fax later'
        # response = pamfax.send_later()
        # _assert_json(message, response)

        # This only works after the fax has moved to the fax history
        # message = 'Cloning the fax'
        # response = pamfax.clone_fax(faxjob['FaxContainer']['uuid'])
        # _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/numberinfo/
    def test_NumberInfo(self):
        message = 'Getting number info'
        response = pamfax.get_number_info('+81362763902')
        _assert_json(message, response)

        message = 'Getting page price'
        response = pamfax.get_page_price('+81362763902')
        _assert_json(message, response)

    # You have to authenticate with a browser first, to do so do as written here:
    # https://sandbox-apifrontend.pamfax.biz/processors/onlinestorage/
    # Don't forget to provide the token you got from your storage provider, e.g. for Dropbox:
    # http://sandbox-api.pamfax.biz/OspAuth/DropboxStorage?usertoken=<your_received_token>
    def test_OnlineStorage(self):
        provider = "DropboxStorage"  # GoogleStorage|DropboxStorage|BoxnetStorage

        # Deactivated, so we don't have to re-authenticate again all the time
        # message = 'Dropping authentication'
        # response = pamfax.drop_authentication('DropBoxStorage')
        # _assert_json(message, response)

        message = 'Checking provider state'
        response = pamfax.check_provider_state(provider)
        _assert_json(message, response)

        message = 'Getting provider logo'
        f, content_type = pamfax.get_provider_logo(provider, 16)
        _assert_file(message, f, content_type)

        message = 'Listing folder contents'
        response = pamfax.list_folder_contents(provider)
        response = _assert_json(message, response, False)
        if response['result']['code'] == 'not_authenticated':
            print('The test for list_folder_contents is skipped, ' \
                  'as it seems you are not authenticated for provider ' + provider + '.\n')
            print('To do so follow the steps on: https://sandbox-apifrontend.pamfax.biz/processors/onlinestorage/')

        # We could also test OnlineStorage::AddFileFromOnlineStorage here.. IFF the user is authenticated AND we got a uuid for a
        # single file (NOT a folder) from OnlineStorage::ListFolderContents AND we created a fax with FaxJob::Create before

        message = 'Listing providers'
        response = pamfax.list_providers()
        _assert_json(message, response)

        # message = 'Setting auth token'
        # response = pamfax.set_auth_token('DropBoxStorage', token)
        # _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/session/
    def test_Session(self):
        message = 'Creating login identifier'
        response = pamfax.create_login_identifier(timetolifeminutes=10)
        _assert_json(message, response)

        message = 'Listing changes'
        response = pamfax.list_changes()
        _assert_json(message, response)

        # message = 'Logging out'
        # response = pamfax.logout()
        # _assert_json(message, response)

        message = 'Pinging'
        response = pamfax.ping()
        _assert_json(message, response)

        message = 'Registering listener'
        response = pamfax.register_listener(['faxsending', 'faxfailed'])
        _assert_json(message, response)

        message = 'Reloading user'
        response = pamfax.reload_user()
        _assert_json(message, response)

        message = 'Verifying user'
        response = pamfax.verify_user(USERNAME, PASSWORD)
        _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/shopping/
    def test_Shopping(self):
        # message = 'Getting invoice'
        # f, content_type = pamfax.get_invoice('')
        # _assert_file(message, f, content_type)

        message = 'Getting nearest fax in number'
        response = pamfax.get_nearest_fax_in_number(IP_ADDR)
        _assert_json(message, response)

        message = 'Getting shop link'
        response = pamfax.get_shop_link('pro_plan')
        _assert_json(message, response)

        message = 'Listing available items'
        response = pamfax.list_available_items()
        _assert_json(message, response)

        message = 'Listing fax in area codes'
        response = pamfax.list_fax_in_areacodes('JP')
        _assert_json(message, response)

        message = 'Listing fax in countries'
        response = pamfax.list_fax_in_countries()
        _assert_json(message, response)

        message = 'Redeeming credit voucher'
        response = pamfax.redeem_credit_voucher('PCPC0815')
        _assert_json(message, response)

    # https://sandbox-apifrontend.pamfax.biz/processors/userinfo/
    def test_UserInfo(self):
        # Can be executed only once, or would require to create randomized names & emails
        # message = 'Creating user'
        # response = pamfax.create_user(name='abc123xyz', username='abc123xyz@gmail.com', password='xyz123abc', email='abc123xyz@gmail.com', culture='en-US')
        # _assert_json(message, response)

        # Dangerous? Would it delete yourself?
        # message = 'Deleting user'
        # response = pamfax.delete_user()
        # _assert_json(message, response)

        message = 'Getting culture info'
        response = pamfax.get_culture_info()
        _assert_json(message, response)

        message = 'Has plan?'
        response = pamfax.has_plan()
        _assert_json(message, response)

        message = 'Listing expirations'
        response = pamfax.list_expirations()
        _assert_json(message, response)

        message = 'Listing inboxes'
        response = pamfax.list_inboxes(expired_too=True, shared_too=True)
        _assert_json(message, response)

        message = 'Listing orders'
        response = pamfax.list_orders()
        _assert_json(message, response)

        message = 'Listing profiles'
        response = pamfax.list_profiles()
        _assert_json(message, response)

        message = 'Listing user agents'
        response = pamfax.list_user_agents(max=2)
        _assert_json(message, response)

        message = 'Listing wall messages'
        response = pamfax.list_wall_messages(count=1)
        _assert_json(message, response)

        message = 'Sending message'
        response = pamfax.send_message('Hello, world!', type='email', recipient='test@example.com', subject='Hello')
        _assert_json(message, response)

        # Commented just to prevent all the reset password emails
        # message = 'Sending password reset message'
        # response = pamfax.send_password_reset_message(USERNAME)
        # _assert_json(message, response)

        message = 'Setting online storage settings'
        response = pamfax.set_online_storage_settings('DropBoxStorage', ['inbox_enabled=1', 'inbox_path=/'])
        _assert_json(message, response)

        # message = 'Setting password'
        # response = pamfax.set_password(PASSWORD, hashFunction='plain')
        # _assert_json(message, response)

        # message = 'Setting profile properties'
        # response = pamfax.set_profile_properties(profile='test', properties=)
        # _assert_json(message, response)

        # Requires an email
        message = 'Validating new username'
        response = pamfax.validate_new_username('kaninchen@hoppel.de')
        _assert_json(message, response)


if __name__ == '__main__':

    run_all = False

    # Either run all tests or en- or disable test packages by (un)commenting
    if run_all:
        unittest.main()
    else:
        suite = unittest.TestSuite()

        suite.addTest(TestPamFax("test_Common"))
        suite.addTest(TestPamFax("test_FaxHistory"))
        suite.addTest(TestPamFax("test_FaxJob"))
        suite.addTest(TestPamFax("test_NumberInfo"))
        suite.addTest(TestPamFax("test_OnlineStorage"))
        suite.addTest(TestPamFax("test_Session"))
        suite.addTest(TestPamFax("test_Shopping"))
        suite.addTest(TestPamFax("test_UserInfo"))

        runner = unittest.TextTestRunner()
        runner.run(suite)
