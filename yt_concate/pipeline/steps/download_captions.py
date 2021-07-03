import os
import time
import urllib.error
import concurrent.futures #使用這個concurrent模組來將multithreading

from pytube import YouTube

from .step import Step
from .step import StepException

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        print('concurrent.futures')
        start = time.time()
        for yt in data:
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue
            try:
                print('downloanding caption for', yt.id)
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')#get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            except AttributeError:
                print('AttributeError when downloading caption for', yt.url)
                continue
            except urllib.error.HTTPError:
                print('urllib.error.HTTPError when downloading caption for', yt.url)
                continue

            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end-start, 'seconds')
        return data









