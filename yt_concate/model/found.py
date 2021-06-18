
class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):#印出簡易資訊
        return '<YT(' + str(self.yt) + ')>'

    def __repr__(self):#印出完整資訊
        content = ' : '.join([
            'yt=' + str(self.yt),
            'caption=' + str(self.caption),
            'time=' + str(self.time),
        ])
        return '<Found(' + content + ')>'