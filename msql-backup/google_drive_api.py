import httplib2
import os

from googleapiclient.http import MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


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
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


def upload_file(
        drive_service, parent_folder_id,  file_name, file_path, mime_type):
    """
    :param drive_service: discovery.build('drive', 'v3', http=http)
    :param parent_folder_id: ID of folder to upload the file
    :param file_name: name of the file
    :param file_path: path to the file
    :param mime_type: mime type of file (ex: image/jpeg)
    :return: File id from Google drive
    """
    file_metadata = {'name': file_name, 'parents': [parent_folder_id]}
    media = MediaFileUpload(file_path,
                            mimetype=mime_type)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file.get('id')


def create_folder(drive_service, parent_folder_id, folder_name):
    """
    :param drive_service: discovery.build('drive', 'v3', http=http)
    :param parent_folder_id: ID of folder to upload the file
    :param folder_name: Name of the folder to be created
    :return:
    """
    file_metadata = {
        'name': folder_name,
        'parents': [parent_folder_id],
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata,
                                          fields='id').execute()
    return folder.get('id')


if __name__ == '__main__':
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
