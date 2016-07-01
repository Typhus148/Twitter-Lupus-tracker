import dropbox
from Dropbox_api_auth import App_secret, App_key, Access_token


def Dropbox_api_app(data):
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(App_key, App_secret)
    client = dropbox.Dropbox(Access_token)
    # print('linked account: ', client.users_get_current_account())
    f = open('fetched_lupus_tweets.txt', 'a')
    # client.files_create_folder('/test_folder'
    # client.files_upload(f, '/fetched_lupus_tweets.txt')
    client.files_upload_session_append_v2(f, data, close=False)
