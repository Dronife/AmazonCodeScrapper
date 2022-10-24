from Service.VideoChecker import VideoChecker
from Service.VideoTextRecognition import VideoTextRecognition

if __name__ == '__main__':
    videoTextRecognition = VideoTextRecognition()
    # videoTextRecognition.captureFrames("https://www.youtube.com/watch?v=2WrX8QMbXMQ")
    videoTextRecognition.video_to_frames_url_auto("https://www.youtube.com/watch?v=2WrX8QMbXMQ")
# videoChecker = VideoChecker()
# if(videoChecker.isLatestVideoNew(timeSearch="hours") and videoChecker.videoIsLaughOrLose()):
#     print("True")
# else:
#     print("false")
    