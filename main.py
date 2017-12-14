
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_unreaded_messages(service, user_id, labels):
    """
        Gmail'den user_id ve labels'e gore mesajlarin id'leri cekilir.
    """
    return service.users().messages().list(
        userId=user_id, labelIds=labels).execute()

def get_message(service, user_id, message_id):
    """
        Gmail'den user_id ve message_id'e gore mesaj cekilir.
    """
    return service.users().messages().get(
            userId=user_id, id=message_id).execute()

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    # Gmailden okunmamis tum mesajlari al.
    unreaded_messages = get_unreaded_messages(service, 'me', ['INBOX', 'UNREAD'])

    messages_list = unreaded_messages['messages']
    messages_amount = len(messages_list)

    #print(messages_list)
    #print(messages_amount)

    # Tum mesajlar daha detayli cekilir.
    for message_obj in messages_list:
        MessageData = {}
        message_id = message_obj['id']

        message = get_message(service, 'me', message_id)

        for header in message['payload']['headers']:
            if header['name'] == 'From':
                MessageData['From'] = header['value']
            if header['name'] == 'Subject':
                MessageData['Subject'] = header['value']
            if header['name'] == 'Date':
                MessageData['Date'] = header['value']
            if header['name'] == 'Content-Type':
                MessageData['Content-Type'] = header['value']

        MessageData['Snippet'] = message['snippet']
        print(MessageData)

if __name__ == '__main__':
    main()
