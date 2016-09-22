import os
import sys


def write_file(filename, text):
    file = open(filename, 'w')
    file.write(text)
    file.close()

    
def main():
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
        write_file(os.path.join(project_name,'build.sbt'), 'name:= "{}"\n\nversion := "1.0"\n\nscalaVersion:= "2.11.8"\n\n'.format(project_name)) 

        scalatest = input("Do you want to add ScalaTest as a dependency?[Y/n] ")

        if(scalatest.lower() == 'y' or scalatest == ''):
            write_file(os.path.join(project_name,'build.sbt'),'libraryDependencies += "org.scalactic" %% "scalactic" % "3.0.0"\n\nlibraryDependencies += "org.scalatest" %% "scalatest_2.11" % "3.0.0" % "test"')
            write_file(os.path.join(project_name, 'project', 'plugins.sbt'),'addSbtPlugin("com.artima.supersafe" % "sbtplugins" % "1.1.0")')

if __name__ == "__main__":
    main()
