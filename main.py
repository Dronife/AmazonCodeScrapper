from Service.VideoChecker import VideoChecker
from Service.VideoDownloader import VideoDownloader
from Service.FrameExtraction import FrameExtraction
import time
if __name__ == '__main__':
    start_time = time.time()
    videoRecog = VideoDownloader()
    videoRecog.downloadVideo("https://www.youtube.com/watch?v=2WrX8QMbXMQ")
    # print(videoRecog.getPath())
    FrameExtraction().video_to_frames(videoRecog.getPath(), "image",False, 60, 6000)
    print("\n--- %s seconds ---" % (time.time() - start_time))
