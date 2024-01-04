
import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
from datetime import timedelta

import isodate
##

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = "AIzaSyATnHuy8xrwVEqk97ZX8B9Gyhsqz_k99T4"

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def print_info(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        self.channel_info = self.get_channel_info()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.channel_description = self.channel_info['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_count != other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    @classmethod
    def get_service(cls):
        return youtube

    def get_channel_info(self):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, file_name):
        channel_data = {
            'channel_id': self.channel_id,
            'channel_title': self.title,
            'channel_description': self.channel_description,
            'channel_link': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file_name, 'w') as file:
            json.dump(channel_data, file)


class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.playlist_info = self.get_playlist_info()
        self.title = self.playlist_info['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.video_count = self.playlist_info['contentDetails']['itemCount']

    def __str__(self):
        return f"{self.title} ({self.url})"

    def get_video_details(self, id, part):
        return youtube.videos().list(part=part, id=id).execute()['items'][0]

    def get_playlist_info(self):
        playlist = youtube.playlists().list(id=self.playlist_id, part='snippet,contentDetails').execute()['items'][0]
        return playlist

    @property
    def total_duration(self):
        duration = timedelta()
        videos = self.get_playlist_videos()
        for video in videos:
            video_details = self.get_video_details(id=video['contentDetails']['videoId'], part='contentDetails')
            duration += timedelta(
                    seconds=isodate.parse_duration(video_details['contentDetails']['duration']).total_seconds())
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        seconds = duration.seconds % 60
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def show_best_video(self):
        videos = self.get_playlist_videos()
        video_details = []
        for video in videos:
            video_details.append(self.get_video_details(id=video['contentDetails']['videoId'], part=['statistics']))
        best_video = max(video_details, key=lambda x: int(x['statistics']['likeCount']))
        return f"https://youtu.be/{best_video['id']}"

    def get_playlist_videos(self):
        videos = []
        next_page_token = None
        while True:
            request = youtube.playlistItems().list(
                playlistId=self.playlist_id,
                part='snippet,contentDetails',
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            videos.extend(response['items'])
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        return videos
