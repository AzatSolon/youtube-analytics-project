import json

from googleapiclient.discovery import build
from dotenv import load_dotenv
from pprint import pprint

import os

load_dotenv('../.env')
api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""
    __youtube = build("youtube", "v3", developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.channel)

    def to_json(self, item):
        """Функция сохраняющая в файл значения атрибутов экземпляра Channel"""
        date = json.dumps(self.channel)
        with open(item, 'w', encoding="utf-8") as file:
            file.write(date)

    @property
    def channel_id(self):
        """Воввращает id  канала"""
        return self.__channel_id

    @property
    def title(self):
        """возвращает название  канала"""
        return f"{self.channel['items'][0]['snippet']['title']}"

    @property
    def video_count(self):
        """Возвращает количество видео"""
        return f"{self.channel['items'][0]['statistics']['videoCount']}"

    @property
    def url(self):
        """Возвращает ссылку на канал"""
        return f"{self.channel['items'][0]['snippet']['thumbnails']['default']['url']}"

    @classmethod
    def get_serves(cls):
        """класс-метод get_service(), возвращающий объект для работы с YouTube API"""
        return cls.__youtube
