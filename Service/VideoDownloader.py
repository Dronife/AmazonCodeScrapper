
import os
from functools import partial
from multiprocessing.pool import Pool
from pytube import YouTube 
import os

import cv2


class VideoDownloader:

    def __init__(self) -> None:
        self.__pathToSaveVideo = "Media/video/"
        self.__pathToSaveImage = r"Media/image/"
        self.__fileName = "video"
        self.__fileExtension ="mp4"
        pass

    def getFileName(self):
        return self.__fileName+"."+self.__fileExtension

    def getPath(self):
        return  self.__pathToSaveVideo+self.getFileName()

    def downloadVideo(self, url):

        yt = YouTube(url)
        yt = yt.streams.filter(progressive=False, file_extension=self.__fileExtension, res="1080p").first()
        print("Starting to download video...")
        # yt.download(self.__pathToSaveVideo,  self.__fileName+"."+self.__fileExtension)
        print("Finished to download video")


       

