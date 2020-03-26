#!/usr/bin/env python
# coding: utf-8




from pytube import YouTube
import os
from pathlib import Path
ans='y'
while(ans=='y'):
    print("Enter URL of the Youtube video to be downloaded")
    link=input()
    print("You have two options to download the video-")
    print("1. Download the Video in 720p HD along with audio")
    print("2. Download the highest resolution in which the video is avaliable whether it be 4K or EVEN 8K,but in this case the audio") 
    print("would be saved separately in a another folder because in resolutions above 720p, youtube does not") 
    print("store and stream the video and audio together, but the video quality in this case would be amazing")
    print()
    print("Enter 1 or 2")
    q=input()
    ab=int(q)
    yt=YouTube(link)
    t=yt.title
    l=[]
    for char in t:
        if (char==" "):
            l.append("_")
        abc=str(char)
        if (abc.isalnum())==False:
            continue
        else:
            l.append(char)
    s=""
    for i in l:
        s=s+i
    t=s
    
    if (ab==1):
        t=t+"720p"
        cwd=Path.cwd()
        a=os.path.join(str(cwd),str(t))
        try:
            os.mkdir(a)
        except OSError as error:
            print("The video that you are trying to download is already present in this directory. Please enter the URL of some new video which has not been downloaded to download it")
        os.chdir(a)
        vid=yt.streams.filter(progressive=True).order_by('resolution')[-1]
        vid.download()
        os.chdir("..")
    
    elif (ab==2):
        t=t+"Highest_Resolution"
        cwd=Path.cwd()
        a=os.path.join(str(cwd),str(t))
        try:
            os.mkdir(a)
        except OSError as error:
            print("The video that you are trying to download is already present in this directory. Please enter the URL of some new video which has not been downloaded to download it")
        os.chdir(a)
        b=os.path.join(a,"Video")
        try:
            os.mkdir(b)
        except OSError as error:
            print("The video that you are trying to download is already present in this directory. Please enter the URL of some new video which has not been downloaded to download it")
        os.chdir(b)
        video=yt.streams.order_by('resolution')[-1]
        video.download()
        os.chdir("..")
        c=os.path.join(a,"Audio")
        try:
            os.mkdir(c)
        except OSError as error:
            print("The video that you are trying to download is already present in this directory. Please enter the URL of some new video which has not been downloaded to download it")
        os.chdir(c)
        audio=yt.streams.filter(only_audio=True).order_by('abr')[-1]
        audio.download()
        os.chdir("..")
        os.chdir("..")
    else:
        print("Wrong Input.... PLease enter 1 or 2 Only")
    print()
    print("Do you want to download more videos y/n")
    ans=input()
    if (ans=='n'):
        break






