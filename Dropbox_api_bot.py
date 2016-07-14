def dropbox_main(data):
    # Use the file path to your dropbox app to save the file.
    file_to = u'/file/path/to/dropbox/app'
    with open(file_to, 'a') as f:
        f.write(data)
