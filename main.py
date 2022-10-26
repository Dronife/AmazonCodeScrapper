from Service.VideoChecker import VideoChecker
from Service.VideoTextRecognition import VideoTextRecognition
import time

start_time = time.time()
videoRecog = VideoTextRecognition()
videoRecog.downloadVideoWithPafy("https://www.youtube.com/watch?v=2WrX8QMbXMQ")
print("\n--- %s seconds ---" % (time.time() - start_time))
