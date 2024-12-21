import os
import shutil

def manage_folder(folder):
    file_types = {
        'Images' : ['.jpg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.csv'],
        'Music': ['.mp3'],
        'Video': [".mp4"],
        'ZipFiles': ['.zip'],

    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        # print(file_path)

        if os.path.isfile(file_path):
            for directory, extensions in file_types.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(folder, directory)
                    # print(folder_path)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {directory}")
                    break

    

manage_folder("E:/manage")

