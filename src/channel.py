from dotenv import load_dotenv
import os
import json
load_dotenv()
from googleapiclient.discovery import build
import json


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = os.getenv('AIzaSyAEGHL40vqEZXrb_WbFZW_M3nRe-LfJ2xY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self):
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=True))