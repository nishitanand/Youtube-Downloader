<h1>YouTube video Downloader</h1>

This project is a long time passion project of mine.

It is a Youtube Video Downloader. Now you don't have to rely on sketchy sites to download videos and can even download 4K Videos which is not an option on such websites.

Here, First the user has to enter the URL of the Video to be downloaded.

Then he will be given 2 options-

Either download the video in 720p along with the audio (as usual)

OR

Download the video in the most highest resolution available on Youtube whether it is 4K or Even 8K.

It uses the PyTube Library and searches for all resolutions available and dowloads 720p or the highest reolution available on the basis of choice by the user

I have also used OS library to use os.mkdir() and os.chdir() to create folders automatically and also Pathlib library to get Path of Current Working Directory. 

Main use of this project was that as we all know the internet sppeds are not that great in India, so we are unable to stream Youtube at 4K resolution, so this project is useful for those Pixel peepers who want to see all the 4K details. 

If the user selects option 2 then the highest Quality gets Downloaded. One drawback is that above 720p, Youtube does not stream and store audio and video together so, the video and audio is stored separately if 2nd option is chosen by the user. Audio and Video are stored in separate folders called "Audio" and "Video".
Even though the video has no audio, but the video quality of 4K is just eye popping and brings joy. A 10 minute 4K Video can be upto 500MB.
If people have time then they can use some 3rd party software to combine the audio and 4K video together and it would be the best of both worlds. 
