
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
