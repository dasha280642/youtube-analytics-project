
import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate
import os


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def print_info(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    def __init__(self, channel_id: str):
        self.channel_id = channel_id

    def get_channel_info(self):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def get_playlists(self):
        playlists = youtube.playlists().list(channelId=self.channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        return playlists

    def get_playlist_videos(self, playlist_id: str):
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def get_video_duration(self, video_id: str):
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=video_id
                                               ).execute()
        iso_8601_duration = video_response['items'][0]['contentDetails']['duration']
        duration = isodate.parse_duration(iso_8601_duration)
        return duration

    def get_video_stats(self, video_id: str):
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        video_title = video_response['items'][0]['snippet']['title']
        view_count = video_response['items'][0]['statistics']['viewCount']
        like_count = video_response['items'][0]['statistics']['likeCount']
        comment_count = video_response['items'][0]['statistics']['commentCount']
        return video_title, view_count, like_count, comment_count


