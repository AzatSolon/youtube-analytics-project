from src.channel import Channel

you_tube_video_api = Channel.get_service()


class Video:
    """
    Класс для работы с видео ютуб :
    - id видео
    - название видео
    - ссылка на видео
    - количество просмотров
    - количество лайков)
    """

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        video = you_tube_video_api.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                 id=video_id
                                                 ).execute()
        try:
            self.video_url: str = f"https://youtu.be/{self.video_id}"
            self.title = video['items'][0]['snippet']['title']
            self.view_count = video['items'][0]['statistics']['viewCount']
            self.like_count = video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    """
    Класс для работы с плейлистами видео:
    - id видео
    - название видео
    - ссылка на видео
    - количество просмотров
    - количество лайков
    - id плейлиста
    """
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{self.title}"
