import json
import xml.etree.ElementTree as et
from typing import Dict, Optional, Union


class JsonSerializer:
    """object to json type serializer"""

    def __init__(self) -> None:
        """initiate object tracking dictionary"""
        self._current_object: Dict[str, str] = {}

    def start_object(self, object_name: str, object_id: str) -> None:
        """add new object to tracker with id

        Args:
            object_id (str): object id
        """
        self._current_object = {"id": object_id}

    def add_property(self, key: str, value: str) -> None:
        """add new property to the object

        Args:
            key (str): property key
            value (str): property value
        """
        self._current_object[key] = value

    def to_str(self) -> str:
        """convert to serialized format

        Returns:
            str: return string formated object
        """
        return json.dumps(self._current_object)


class XmlSerializer:
    """object to xml serializer"""

    def __init__(self):
        """initialize object tracker"""
        self._element = None

    def start_object(self, object_name: str, object_id: str):
        """initialize object with xml element

        Args:
            object_name (str): name of object
            object_id (str): object id
        """
        self._element = et.Element(object_name, attrib={"id": object_id})

    def add_property(self, key: str, value: str):
        """add new properties to the objects

        Args:
            name (str): key of the property
            value (str): value of the property
        """
        prop = et.SubElement(self._element, key)  # type: ignore
        prop.text = value

    def to_str(self) -> str:
        """convert to serializable format

        Returns:
            str: string formatted output
        """
        return et.tostring(self._element, encoding="unicode")  # type: ignore
