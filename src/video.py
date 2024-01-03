class Video:
    def __init__(self, video_id):
        self.id = video_id

        self.title = 'GIL в Python: зачем он нужен и как с этим жить'
        self.link = f'https://www.youtube.com/watch?v={video_id}'
        self.views = 1000
        self.like_count = 50

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

