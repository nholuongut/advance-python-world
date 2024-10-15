from serializers import JsonSerializer, XmlSerializer
from typing import Union


class Song:
    """define song object"""

    def __init__(self, song_id: str, title: str, artist: str):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def add_property(self, serializer: Union[JsonSerializer, XmlSerializer]) -> None:
        """add new properties to song

        Args:
            serializer (Union[JsonSerializer, XmlSerializer]): serializer object
        """
        serializer.start_object(object_name="song", object_id=self.song_id)
        serializer.add_property(key="title", value=self.title)
        serializer.add_property(key="artist", value=self.artist)
