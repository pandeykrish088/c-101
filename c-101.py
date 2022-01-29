import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BBBWhhPNNZwznmey1pzsbNilu8g1CvT7F49_mxsZjpSXmlWyqe-_PvqGF3v7nrA3Cwwq5YmpRh8osCAgRIhAngbiuah8uq0m-D3lOJL03eKCJoaDD1QwME5FgcNAWAUhLCb_nCo'
    transferData = TransferData(access_token)

    file_from = input('Enter the File path to Transfer')
    file_to = input('enter the File path to upload Dropbox')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    print('File has been Moved')

main()
