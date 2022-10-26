from Service.VideoChecker import VideoChecker
from Service.VideoTextRecognition import VideoTextRecognition
import time
start_time = time.time()

videoRecog = VideoTextRecognition()
videoRecog.downloadVideo()

print("\n--- %s seconds ---" % (time.time() - start_time))
