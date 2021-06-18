import urllib.error

from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR



class DownloadVideo(Step):
    def process(self, data, inputs, utils):


            print(len(data))
            yt_set = set([found.yt for found in data])#set刪除重複
            print('video to download', len(yt_set))



            for yt in yt_set:
                url = yt.url
                if utils.video_file_exists(yt):
                    print(f'found existing video file for {url}, skipping' )
                    continue

                try:
                    print('downloading ', url)
                    YouTube(url).streams.first().download(output_path= VIDEOS_DIR, filename= yt.id)

                except urllib.error.HTTPError:
                    print('urllib.error.HTTPError when downloading caption for', url)
                    continue

            return data