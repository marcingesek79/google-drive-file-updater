from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# Enter your file path
my_file_path = ""

# Enter your file name
my_file_name = ""

# Do you want to thrash or delete the file?
# True = delete
# False = trash
choice = False

auth = GoogleAuth()
auth.LocalWebserverAuth()
drive = GoogleDrive(auth)

if my_file_path and my_file_name:

    # Deleting file
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in file_list:
        if file['title'] == my_file_name:
            if not choice:
                file.Trash()
            elif choice:
                file.Delete()

    # Uploading file
    file = drive.CreateFile({'title': my_file_name})
    file.SetContentFile(my_file_path)
    file.Upload()
