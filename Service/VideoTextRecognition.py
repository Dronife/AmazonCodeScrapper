
import os
from functools import partial
from multiprocessing.pool import Pool
from pytube import YouTube 

import cv2
import youtube_dl


class VideoTextRecognition:

    def __init__(self) -> None:
        pass

    def downloadVideo(self, url):

        yt = YouTube(url)
        # print(yt.streams)
        yt = yt.streams.filter(progressive=False, file_extension='mp4', res="1080p").first()
        yt.download("Media/VIDEO")

    def process_video_parallel(self, url, skip_frames, process_number):
        cap = cv2.VideoCapture(url)
        num_processes = 1
        frames_per_process = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, 2000)
        x = 0
        count = 0
        while x < 10 and count < frames_per_process:
            ret, frame = cap.read()
            if not ret:
                break
            filename =r"SHOTS/image"+str(x)+".png"
            x += 1
            # resize = cv2.resize(frame, (1280, 720))
            cv2.imwrite(filename.format(count), frame)
            count += skip_frames  # Skip 300 frames i.e. 10 seconds for 30 fps
            cap.set(1, count)
        cap.release()

    def captureFrames(self, video_url):
        ydl_opts = {}
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(video_url, download=False)

        formats = info_dict.get('formats', None)

        print("Obtaining frames")
        for f in formats:
            if f.get('format_note', None) == '720p':
                url = f.get('url', None)
                cpu_count = os.cpu_count()
                with Pool(cpu_count) as pool:
                    pool.map(partial(self.process_video_parallel, url, 60), range(cpu_count))

    def video_to_frames_url_auto(self, url=None, folder='/Users/Deimantas/Desktop/YoutubeScrapper/VIDEO/'):
        """Function to extract frames from input video url or file and save them as separate frames 
        in an output directory. Output directory will be named starting from video_1. If a new file is downloaded,
        a video_2 folder will be created and so on.
        Dependencies: 
            OpenCV
            youtube-dl (sudo pip install --upgrade youtube_dl)
        
        Args:
            url: Youtube video URL.
            folder: Directory to download and save each frames.
            
        Returns:
            None
            
        Work to be done:
        1. Handle exceptions
        """
        import os
        import re
        import cv2
        import time
        
        # Log start time
        time_start = time.time()
        
        # To make a directory for saving video automatically considering all the existing foldernames
        reg = re.compile(r'^video_')
        lst = sorted(os.listdir(folder))
        newlist = filter(reg.match, lst)
        numbers = [reg.sub('', x).strip() for x in newlist]
        results = map(int, numbers)
        results = sorted(results)
        newfile = "laugh_video"
        # Make a directory for the video
        # If no video's exist as of now, create a folder.
        if(results == None):
            os.mkdir("video_1")
        # Create a folder according to the files that are already present.   
        os.mkdir("video_" + str(newfile))
        
        file_loc = folder + "video_" + str(newfile) + "/video_" + str(newfile) + ".mp4"
        # Download from local video file
        if (url):
            print("Downloading Youtube Video")
            os.system("youtube-dl -o " + file_loc + " -f mp4 " + url)
            cap = cv2.VideoCapture(file_loc)
        else:
            print("This is where I should raise an error. --EXCEPTION HANDLING--")

        video_length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)) - 1
        print ("Number of frames: ", video_length)
        count = 0
        print ("Converting video..\n")
        while cap.isOpened():
            ret,frame = cap.read()

            cv2.imwrite(folder + "video_" + str(newfile) + "/%d.jpg" % (count+1), frame)
            count = count + 1
            if (count > (video_length-1)):
                time_end = time.time()
                cap.release()
                print ("Done extracting frames.\n%d frames extracted" %count)
                print ("It took %d seconds for conversion." %(time_end-time_start))
                break

