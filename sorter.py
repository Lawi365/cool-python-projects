#! python3.7

"""
  This program sorts file in the donwload folders to the relevant files.
  Music files will be moved to music folder
  Softwares will also be moved to software folder
  videos will be moved to video folder.

  version 1.1
  author T@rminal.
  project no. 001
  dec holiday...(two weeks)

  If a music file is contained in a folder i.e a folder that contains only music
  then the program will move the entire content of the folder to the relevant folder.

  what if their is an unrecognised files eg videoplayback(1....etc)
  the program should create an identified folder called UNKOWN/UNPLACED
  for the sake of tidiness of the download folder.

  The program will mainly operate on the user's folder just to ensure that it doesn't 
  mess with your programs files...

  ========================update to contain====================
  
    1. Ability to merge related music files in one folder.
       based on the singer name.
    
    2. Ability to notify the user of the best place to place his/her files.

    3. Ability to ... (okay) i dont know.


"""

import os, re
import time

my_path = {}
music_list = []
software_list = []
video_list = []
path=r"C:\users\lecnac\desktop"

def lister():
    """
     This function walks through the user folders and determines the type of files
     in those folders.
     If the file is music it renames the music
     and so with the other files types.

    """

    for folders, subfolders, files in  os.walk(path):
        
        for file in files:
            if file.endswith('.mp3'):
                music_list.append(file)
                print(folders)

            if file.endswith('.exe'):
                software_list.append(file)
                pass
            
            if file.endswith('.mp4'):
                video_list = []
                pass

            else:
                pass

    print("==========Done=========")
    

def filename_renamer():
    """
    This function just functions figure out why.
    first 
    """
    print(os.chdir(path))

    try:
        
        for i in music_list:

            start = my_regex(i)
            end = i[:start]
            dst = (end+".mp3")

            print(i+"\n")

            # now the place where the renaming is done.
            try:
                os.replace(i, dst)
                
            except FileNotFoundError:
                
              print("file not found")

    except AttributeError:
        pass



def rename_hyphen():
    """ 
        The new file now does'nt contain the words after the _
        now we want to remove the -.

    """
    print(path)
    #os.chdir(os.getcwd()+ "\\test_data")

    print(music_list)
    
    for i in music_list:
        j = i 
        j = j.split('-')

        j = ' '.join(j)
        j = j.strip()

        os.replace(i, j)

  
def my_regex(parameter):
    
    """
    This function defines the regex that will be used to remove the giberish words
    It retuns the location where the word starts at.

    """
    my_regex = re.compile(r"Official|[_]|(")

    result = my_regex.search(parameter)
    
    if result.group() != 'none':
         return result.start()
    
    else:
        return ''

lister()

#newfiles = os.listdir()
#for i in newfiles:
    #print(i)
