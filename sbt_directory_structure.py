import os
import sys

root_path = 'src/'
folders = ['main', 'test']
subfolders = ['resources', 'scala', 'java']
root_folders = ['lib', 'project']
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    for folder in folders:
        for subfolder in subfolders:
            try:
                os.makedirs(os.path.join(root_path, folder, subfolder))
            except:
                if FileExistsError:
                    pass
                else:
                    print(e)
    for i in root_folders:
        os.mkdir(os.path.join(root_path, i))
                 
if sys.platform.startswith('win32'):
    pass
