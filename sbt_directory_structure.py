import os
import sys

root_path = 'src/'
folders = ['main', 'test']
subfolders = ['resources', 'scala', 'java']
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
if sys.platform.startswith('win32'):
    pass
