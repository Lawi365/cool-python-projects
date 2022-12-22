#!python3

"""
Youtube is multi purposesd youtube file downloader.

version 0.0.1
author @terminal
date jan 14/2020

With simple yet no elegant look, all it needs is just the
youtube file link and kachaaaa! e rest is history.
If the text copied on the clip board is a youtube link
and provided their is internet this program will automaticaly start
the file download.
It doesn't matter if the files is a youtube playlist or just a single file.
it will download it/them.
Thank me later (+_+)

"""

import pyperclip, os, sys, time, re
from pytube import YouTube
import urllib.request as conn


class youtube:

    def __init__(self, yLink, downloaded, date, connection, isdownloading, flag):
        
        self.yLink = ''
        self.downloaded = False
        self.date = date
        self.connection = False
        self.isdownloading = False
        self.flag = flag
    
    def link_regex(self, your_link):

        regex = re.compile(r'https://youtu.be/*')

        result = regex.search(your_link)

        try:

            result.start()
            self.flag = True
            self.yLink = your_link[result.start:result.start+28]

        except AttributeError:

            self.flag = False

    def get_link_clipboard(self):

        """
        This code gets the text currently in the clipboard
        it executes continously until a link is found.
        After which the link wil be written into a download.txt
        by default.

        """
        while True:
            link = pyperclip.paste()
            link_regex(link)

            if self.flag:
                
                """global vid_list = []"""

                vid_list.append(ylink)
                
                with open('download.txt','a') as file:
                    for i in vid_list:
                        file.write(i)
                    

    def check_disk_space(self):

        """
        The code checks if their is enough disk space to download the file.
        if their is isn't enough disk space it will prompt the user to free space.

        """
    def check_connection(self):
        try:
            conn.urlopen(r"https://google.com")
            self.connection = True
        except:
            pass
            raise

    def download_file(self):

        """
        It download the files.
        If it happens that the internet is up and active the files in
        download.txt will start to download one after the other.

        """

        if self.connection:
            
            with open('download.txt', 'r') as file:
                try:
                    mylist = file.readlines()
                
                except:
                    pass
                    raise
            
       # mylist = mylist.split


#additional functionality will be added as urgency increases.