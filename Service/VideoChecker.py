
import scrapetube

class VideoChecker:

    def __init__(self, channelUrl = "") -> None:
        self._imageToTest = "https://i.postimg.cc/4xJJQ1vP/image.png"
        self.__testThumbnail = "https://i.ytimg.com/vi/2WrX8QMbXMQ/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC-cZcnEZsdW2cH9rvzc3q8fP-J-Q"
        self.__channelUrl = "https://www.youtube.com/c/DharMannOfficial"
        self.__thumbnails = []
        self.__videoId = ""
        self.__videoUrl = ""
        if(channelUrl):
             self.__channelUrl = channelUrl
        pass
    
    
    def imageToTestKeras(self) -> None:
        import matplotlib.pyplot as plt
        import keras_ocr

        pipeline = keras_ocr.pipeline.Pipeline()
        images = [keras_ocr.tools.read(url) for url in [self._imageToTest]]
        prediction_groups = pipeline.recognize(images)
        predicted_image = prediction_groups[0]
        for text, box in predicted_image:
            print(text)


    def getVideoId(self):
        return self.__videoId

    def getVideoUrl(self): 
        return self.__videoUrl

    def isLatestVideoNew(self, timeSearch = "days") -> bool:
        videos = scrapetube.get_channel(channel_url=self.__channelUrl, sort_by="newest", limit=1)

        for video in videos:
            if(not timeSearch in (video['publishedTimeText']['simpleText'])):
                return False
            else:
                self.__thumbnails.append(video['thumbnail']['thumbnails'][0]['url'])
                self.__videoUrl = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                return True
        return False

    def setTestThumbnail(self):
        self.__thumbnails.append(self.__testThumbnail)

    def videoIsLaughOrLose(self) -> bool:
        import matplotlib.pyplot as plt
        import keras_ocr

        pipeline = keras_ocr.pipeline.Pipeline()
        images = [keras_ocr.tools.read(url) for url in self.__thumbnails]
        prediction_groups = pipeline.recognize(images)
        for predicted_image in prediction_groups:
            try:
                if any("laugh" in i[0] for i in predicted_image):
                    return True
                else:
                    return False
            except:
                return False
