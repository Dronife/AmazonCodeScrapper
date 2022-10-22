from Service.VideoChecker import VideoChecker

videoChecker = VideoChecker()
videoChecker.setTestThumbnail()
print(videoChecker.videoIsLaughOrLose())