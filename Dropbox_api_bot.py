import dropbox
from Dropbox_api_auth import Access_token
# App_secret, App_key,


def Dropbox_api_app():
    # flow = dropbox.client.DropboxOAuth2FlowNoRedirect(App_key, App_secret)
    # client.files_create_folder('/test_folder'
    # print('linked account: ', client.users_get_current_account())
    client = dropbox.Dropbox(Access_token)
    f = open('fetched_lupus_tweets.txt', 'rb')
    client.files_upload(f, '/fetched_lupus_tweets.txt')
    # client.files_upload_session_append_v2(f, cursor=, close=False)
