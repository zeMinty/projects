from requests import get, post
from parsel import Selector
from datetime import datetime as dt
from re import split


class TTdownloader(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Tiktok downloader/v1.0 (thank you)",
        }
        self.apiUrl = "https://tikcd.com/en/video/info"

    def __videoUrlByText(self, html, text):
        pattern = f'//div[@class="tiktok-downloader-button-container"]//a[@class="tiktok-downloader-button"][text()="{text}"]/@href'
        videoUrl = html.xpath(pattern).get()
        return videoUrl

    def __getVideoUrl(self, tiktokUrl, mode):
        params = {"url": tiktokUrl}
        result = post(self.apiUrl, headers=self.headers, data=params)
        html = Selector(result.text)
        videoUrlList = {
            "videoHD": self.__videoUrlByText(html, "Without watermark HD"),
            "video": self.__videoUrlByText(html, "Without watermark"),
            "audio": self.__videoUrlByText(html, "Download MP3"),
        }
        return videoUrlList[mode]

    def getBytes(self, tiktokUrl=None, mode="videoHD"):
        if tiktokUrl is None:
            raise ValueError("/getBytes: No url given!")

        videoUrl = self.__getVideoUrl(tiktokUrl, mode)
        video = get(videoUrl)
        return video.content

    def download(self, tiktokUrl=None, filename=None, mode="videoHD"):
        if tiktokUrl is None:
            raise ValueError("/download: No url given!")
        if filename is None:
            ds = split(r"[^\d]+", str(dt.now()))  # date sepparated
            filename = f"tiktok_{ds[0]}{ds[1]}{ds[2]}_{ds[3]}{ds[4]}{ds[5]}.mp4"

        video = self.getBytes(tiktokUrl, mode)
        with open(filename, "wb") as file:
            file.write(video)
