

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'remove this messege and write it here'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/C101_FileTransfer/test.txt'  

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

if __name__ == '__main__':
    main()
