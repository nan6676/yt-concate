import sys
#sys.path.append('../')
import getopt


from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_video import DownloadVideo
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA' #UCeumFHHpVH6DO4ZUlY0mnNw, UCKSVUHI9rbbkXhvAXK-2uxA

def print_usage():
    print('python main.py -c <channel_id> -s <search_word> -l <int(limit)>')
    print('python3.8 yt-concate OPTIONS')
    print('OPTIONS')
    print('{:>6}{:<12}{}'.format('-c ', '--channel', 'channel id of the youtube channel id to download'))
    print('{:>6}{:<12}{}'.format('-s ', '--search', 'search in options of word to download videos'))
    print('{:>6}{:<12}{}'.format('-l ', '--limit', 'concate of download video limit'))

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 40,
    }

    short_opts = "hc:s:l:"
    long_opts = ["help", "channel=", "search=", "limit="]
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        # print help information and exit:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit(2)
        elif opt in ("-c", "--channel"):
            inputs['channel_id'] = str(arg)
        elif opt in ("-s", "--search"):
            inputs['search_word'] = str(arg)
        elif opt in ("-l", "--limit"):
            inputs['limit'] = int(arg)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideo(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(video_list)
