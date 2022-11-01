from Service.VideoChecker import VideoChecker
# from Service.VideoDownloader import VideoDownloader
# from Service.FrameExtraction import FrameExtraction
import time
start_time = time.time()
vd = VideoChecker()
vd.setTestThumbnail()
print(vd.imageToTestKeras())
print("--- %s seconds ---" % (time.time() - start_time))
