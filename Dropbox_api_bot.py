import dropbox
from Dropbox_api_auth import Access_token
# App_secret, App_key,


class Transfer_Data:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2"""
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f, file_to, mode=dropbox.files.WriteMode.overwrite)
            # No idea why files is not is not recognized yet the program still runs and updates the file properly


def dropbox_main():
    transfer_Data = Transfer_Data(Access_token)

    file_from = 'fetched_lupus_tweets.txt'
    file_to = u'/fetched_lupus_tweets.txt'  # The full path to upload the file to, including the file name
    # API v2
    transfer_Data.upload_file(file_from, file_to)

