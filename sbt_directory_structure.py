import os
import sys

if len(sys.argv) < 2:
    project_name = input('Enter a project name: ')
else:
    project_name = sys.argv[1]


root_path = os.path.join(project_name, 'src/')
folders = ['main', 'test']
subfolders = ['resources', 'scala', 'java']
root_folders = ['lib', 'project']


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
    try:
        os.mkdir(os.path.join(project_name, i))
    except:
        if FileExistsError:
            pass
        else:
            print(e)

file = open(os.path.join(project_name,'build.sbt'), 'w')
file.write('name:= "{}"\nversion := "1.0"\nscalaVersion:= "2.11.8"'.format(project_name))
file.close()
