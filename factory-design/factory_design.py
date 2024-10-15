# In serializer_demo.py

import json
import xml.etree.ElementTree as et
from typing import Dict, Optional, Union, Any
from serializers import JsonSerializer, XmlSerializer
from factory import ObjectFactory
from songs import Song

"""
opportunities to user factory method

1. replacing complex logical code 
    Complex logical structures in the format if/elif/else are hard to maintain 
    because new logical paths are needed as requirements change.

2. Constructing related objects from external data
3. Supporting multiple implementations of the same feature
4. Combining similar features under a common interface
"""


class ObjectSerializer:
    # Client Component ( method is the application code that depends on an interface to complete its task)
    def serialize(self, serializable: Song, format: str) -> str:
        """complex if/elif/else logic
        main disadvantage of below is that this method need to change based
        on different aspects like adding new format/song object changes/ format string change
        base on ----- Single Responsibility Principle ---- we only add single
        task for a method/function

        identify the goal
            input : song
            output : serialize object

        create a common interface to handle that
        """

        """basic object serializer

        Returns:
            _str_: serialized string object
        """
        # get the desired serializable method
        serializer = object_factory.get_serializer(format=format)
        # add properties to the serializer
        serializable.add_property(serializer)
        # convert to string format
        return serializer.to_str()


def main():
    pass


if __name__ == "__main__":
    # initialize the object factory
    object_factory = ObjectFactory()

    song = Song("1", "Water of Love", "Dire Straits")
    # intialize object serializer
    serializer = ObjectSerializer()

    print("Json format : \n", serializer.serialize(song, "JSON"))

    print(" xml format : \n", serializer.serialize(song, "XML"))

    serializer.serialize(song, "YAML")
